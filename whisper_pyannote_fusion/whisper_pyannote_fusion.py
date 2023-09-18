import json
import textwrap

import torch
import pyannote
import whisper
import os
import logging
from pyannote.audio import Pipeline

from .fusion_methods import fuse_add_speaker_to_whisper_segments, \
    fuse_add_transcript_to_pyannote_segments, \
    fuse_whisper_words_to_pyannote, fuse_run_whisper_on_pyannote_segments, fuse_word_corrections, \
    run_whisperx_alignment, whisperx_align


def convert_diarization_to_json(diaraization_result: pyannote.core.annotation.Annotation):
    """
    Convert the diarization result to json
    :param diaraization_result: Diarization result from pyannote
    :return: JSON string
    """

    diarization_dict = {
        'speakers': [],
        'segments': []
    }
    speakers_set = set()

    for segment, label, speaker in diaraization_result.itertracks(yield_label=True):
        speakers_set.add(speaker)
        diarization_dict['segments'].append({
            'start': segment.start,
            'end': segment.end,
            'speaker': speaker
        })

    # Convert dictionary to JSON
    diarization_dict['speakers'] = list(speakers_set)
    diarization_json = json.dumps(diarization_dict)

    return diarization_json


def run_pyannote(audio_file, HUGGING_FACE_API_KEY):
    """
    Given the audio file, run pyannote on it
    :param audio_file: Audio file that we want to process
    :return: JSON information of the pyannote result
    """
    pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization',
                                        use_auth_token=HUGGING_FACE_API_KEY)
    pipeline.to(torch.device("cuda"))
    diarization = pipeline(audio_file)
    json_output = convert_diarization_to_json(diarization)

    return json_output


def run_whisper(mp3_filename, initial_prompt):
    """
    Run whisper on the mp3 file and save the result to a json file
    :param mp3_filename: Input file that we want to run whisper on
    :param initial_prompt: Initial prompt that has information about the podcast to decode names and acronyms
    :return: None
    """
    # Load the model
    model = whisper.load_model("large-v2")

    # Load the audio file
    audio = whisper.load_audio(mp3_filename)
    result = model.transcribe(audio, word_timestamps=True, initial_prompt=initial_prompt)

    return result


def convert_seconds_to_hms(seconds):
    # Calculate hours, minutes, and remaining seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the result as a string
    return f"{int(hours)}h {int(minutes)}m {seconds:.2f}s"


def transcript_to_workdown(transcript, md_file):
    """
    Given the transcript data, convert it to markdown
    : param transcript: Transcript data
    : param md_file: Markdown file to write the output to
    """
    with open(md_file, "w") as f:
        # Convert the transcript to markdown
        dialogs = transcript['dialogs']
        for segment in dialogs:
            segment_text = segment['text']
            segment_text = textwrap.fill(segment_text, 80)
            start_time_string = convert_seconds_to_hms(segment['start'])
            end_time_string = convert_seconds_to_hms(segment['end'])
            time_range_str = start_time_string + '-' + end_time_string
            speaker = transcript['speakers'][segment['speaker']]
            f.write('__' + speaker + '__' + ' _(' + time_range_str + '_):\n\n')
            f.write(segment_text + '\n\n')


def whisper_pyannote_fusion(audio_file, method, whisper_json_file=None, pyannote_json_file=None,
                            pyannote_whisper_json_filename=None, whisperx_alignment_json_filename=None,
                            output_json_file=None, corrected_json_file=None,
                            log_file=None, initial_prompt=None, HUGGING_FACE_API_KEY=None):
    """
    Given the audio file, run whisper and pyannote and then fuse the results
    :param audio_file: Audio file that we want to transcribe and diarize
    :param method: Method to use for fusion
    :param whisper_json_file: JSON file of the whisper result if it exists, or we want to save it
    :param pyannote_json_file: JSON file of the pyannote result if it exists, or we want to save it
    :param pyannote_whisper_json_filename: JSON file of the fusion result if we want to save it
    :param whisperx_alignment_json_filename: JSON file of the fusion result if we want to save it
    :param output_json_file: JSON file of the fusion result if we want to save it
    :param corrected_json_file: JSON file that corrects the older output json file
    :param log_file: Log file to save the logs to
    :param initial_prompt: Initial prompt that has information about the audio file to decode names and acronyms
    :param HUGGING_FACE_API_KEY: API key for hugging face
    :return: JSON file of the fusion result with the transcript and diarization
    """

    # Configure logging
    logger = logging.getLogger('fusion_logger')
    logger.setLevel(level=logging.INFO)

    # Check if logger has a stream handler. If so, clear it out and just use new ones for this run
    if len(logger.handlers) > 0:
        logger.handlers.clear()

    # Create a handler for outputting log messages to a stream
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Add a file handler for outputting log messages to a file
    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)

    # Set the json data to be None
    pyannote_json = None
    whisper_json = None
    corrected_json = None
    final_result = None

    # Run pyannote on the audio file depending on the method
    if method in {'pyannote_to_whisper', 'whisper_to_pyannote', 'whisper_words_to_pyannote',
                  'pyannote_segment_run_whisper', 'correct_pyannote_with_whisper', 'whisperx_align_pyannote'}:
        # Check if the pyannote json file exists and if not run pyannote
        if pyannote_json_file is None or not os.path.exists(pyannote_json_file):
            pyannote_json = run_pyannote(audio_file, HUGGING_FACE_API_KEY)
            if pyannote_json_file is not None:
                with open(pyannote_json_file, 'w') as f:
                    f.write(pyannote_json)
        else:
            with open(pyannote_json_file, 'r') as f:
                pyannote_json = json.load(f)

    # Run whisper on the audio file depending on the method
    if method in {'pyannote_to_whisper', 'whisper_to_pyannote', 'whisper_words_to_pyannote',
                  'correct_pyannote_with_whisper', 'whisperx_align_pyannote'}:
        # Check if the whisper json file exists and if not run whisper
        if whisper_json_file is None or not os.path.exists(whisper_json_file):
            whisper_json = run_whisper(audio_file, initial_prompt=initial_prompt)
            if whisper_json_file is not None:
                with open(whisper_json_file, 'w') as f:
                    json.dump(whisper_json, f)
        else:
            with open(whisper_json_file, 'r') as f:
                whisper_json = json.load(f)

    # Fuse the results
    if method == 'pyannote_to_whisper':
        # Check that whisper_json and pyannote_json are not None
        if whisper_json is None or pyannote_json is None:
            raise ValueError('whisper_json and pyannote_json cannot be None')
        final_result = fuse_add_speaker_to_whisper_segments(whisper_json, pyannote_json)
    elif method == 'whisper_to_pyannote':
        # Check that whisper_json and pyannote_json are not None
        if whisper_json is None or pyannote_json is None:
            raise ValueError('whisper_json and pyannote_json cannot be None')
        final_result = fuse_add_transcript_to_pyannote_segments(whisper_json, pyannote_json)
    elif method == 'whisper_words_to_pyannote':
        # Check that whisper_json and pyannote_json are not None
        if whisper_json is None or pyannote_json is None:
            raise ValueError('whisper_json and pyannote_json cannot be None')
        final_result = fuse_whisper_words_to_pyannote(whisper_json, pyannote_json)
    elif method == 'pyannote_segment_run_whisper':
        # Check that pyannote_json is not None
        if pyannote_json is None:
            raise ValueError('pyannote_json cannot be None')
        final_result = fuse_run_whisper_on_pyannote_segments(pyannote_json, audio_file,
                                                             pyannote_whisper_json_filename, HUGGING_FACE_API_KEY,
                                                             initial_prompt=initial_prompt)
    elif method == 'correct_pyannote_with_whisper':
        # Check that pyannote_json is not None
        if pyannote_json_file is None:
            raise ValueError('pyannote_json cannot be None')
        final_result = fuse_run_whisper_on_pyannote_segments(pyannote_json, audio_file,
                                                             pyannote_whisper_json_filename, HUGGING_FACE_API_KEY,
                                                             initial_prompt=initial_prompt)
        corrected_json = fuse_word_corrections(whisper_json, final_result, logger=logger, initial_prompt=initial_prompt)
    elif method == 'whisperx_align_pyannote':
        if not os.path.exists(whisperx_alignment_json_filename):
            whisperx_alignment_json = run_whisperx_alignment(whisper_json=whisper_json,
                                                             audio_filename=audio_file)
            with open(whisperx_alignment_json_filename, 'w') as f:
                json.dump(whisperx_alignment_json, f, indent=2)
        else:
            with open(whisperx_alignment_json_filename, 'r') as f:
                whisperx_alignment_json = json.load(f)

        # Fuse the data and get the transcript output
        final_result = whisperx_align(pyannote_json, whisperx_alignment_json)
    else:
        raise ValueError('Unsupported method')

    # Write the result to a json file if the output file is specified
    if corrected_json is not None:
        if corrected_json_file is not None:
            with open(corrected_json_file, 'w') as f:
                json.dump(corrected_json, f)
        return corrected_json

    if output_json_file is not None:
        with open(output_json_file, 'w') as f:
            json.dump(final_result, f)
    if final_result is not None:
        return final_result
