import json
import os

import jellyfish
import numpy as np
import spacy
import string
import torch
import whisper
import whisperx
from intervaltree import Interval, IntervalTree
from pyannote.audio import Pipeline

from .interval_utils import get_largest_intersection_segment, get_closest_intersection_segment, \
    intersection_length
from .wer import calc_wer_backtrace_words

# Sampling rate used by whisper internally after the audio file has been loaded
WHISPER_SAMPLE_RATE = whisper.audio.SAMPLE_RATE


def get_closest_pyannote_segment(pyannote_tree, whisper_segment):
    """
    Get the pyannote segment that has the largest intersection with the whisper segment
    :param pyannote_tree: Interval tree for pyannote segments
    :param whisper_segment:  Whisper segment
    :return: Segment with the largest intersection
    """
    return get_largest_intersection_segment(pyannote_tree, whisper_segment)


def join_segments(pyannote_segments):
    """
    Join segments that have the same speaker
    :param pyannote_segments: List of pyannote segments
    :return: Joined segments
    """

    pyannote_segments_clean = [pyannote_segments[0]]
    for i in range(1, len(pyannote_segments)):
        pyannote_segment = pyannote_segments[i]
        if pyannote_segment['speaker'] == pyannote_segments_clean[-1]['speaker']:
            pyannote_segments_clean[-1]['end'] = pyannote_segments[i]['end']
        else:
            pyannote_segments_clean.append(pyannote_segment)
    return pyannote_segments_clean


def fuse_add_speaker_to_whisper_segments(whisper_json, pyannote_json):
    """
    Do fusion of the speaker and whisper segments by adding the speaker segments to the whisper segments by finding the
    closest whisper segment to the speaker segment and adding the speaker segment to the whisper segment
    :param whisper_json: Loaded json file for whisper
    :param pyannote_json: Loaded json file for pyannote
    :return: Dictionary with the fused segments with speaker information
    """

    # Join the pyannote segments
    pyannote_json_segments = join_segments(pyannote_json['segments'])

    # Create a interval tree for the pyannote segments
    pyannote_tree = IntervalTree()
    for segment in pyannote_json_segments:
        pyannote_tree.addi(segment['start'], segment['end'], segment)

    # This is the list of the fused dialogs
    dialogs = []

    # Iterate over the whisper segments
    for whisper_segment in whisper_json['segments']:
        # Get the pyannote segment that is closest to the whisper segment
        pyannote_segment = get_closest_pyannote_segment(pyannote_tree, whisper_segment)

        # Add the speaker information to the whisper segment
        speaker_index = pyannote_json['speakers'].index(pyannote_segment.data['speaker'])

        # Add the result to the dialog
        dialogs.append({'speaker': speaker_index, 'start': whisper_segment['start'], 'end': whisper_segment['end'],
                        'text': whisper_segment['text']})

    return {'dialogs': dialogs, 'speakers': pyannote_json['speakers']}


def get_whisper_transcript(whisper_tree, pyannote_segment):
    """
    Get the whisper transcript for the pyannote segment
    :param whisper_tree: Interval tree for whisper segments
    :param pyannote_segment: Pyannote segment
    :return: Whisper transcript for the pyannote segment
    """
    # Get all the overlapping segments to the pyannote_segment
    pyannote_interval = Interval(pyannote_segment['start'], pyannote_segment['end'])

    # Find all the intersecting segments
    intersecting_segments = list(whisper_tree.overlap(pyannote_interval))

    # Get the size of the intersection for each interesting segment
    intersecting_segments_lengths = [intersection_length(segment, pyannote_interval) for segment in
                                     intersecting_segments]

    # This is the time that the segment must intersect to be added to be added to the pyannote segment
    segment_intersection_threshold = 0.5

    # Get the transcript from the whisper segments that intersect with the pyannote segment over the threshold
    intersecting_segments_text = [segment.data['text'] for segment, length in
                                  zip(intersecting_segments, intersecting_segments_lengths) if
                                  length > segment_intersection_threshold]

    # If there are no intersecting segments, then return an empty string
    if len(intersecting_segments_text) == 0:
        return ''
    else:
        # Join the segments with a space
        return ' '.join(intersecting_segments_text)


def fuse_add_transcript_to_pyannote_segments(whisper_json, pyannote_json):
    """
    Do fusion by starting out with pyannote segments and adding the whisper segments to the pyannote segments by finding
    the closest whisper segment
    :param whisper_json: Loaded json file for whisper
    :param pyannote_json: Loaded json file for pyannote
    :return: Dictionary with the fused segments with speaker information
    """

    dialogs = []

    # Add all the whisper segments to the interval tree
    whisper_tree = IntervalTree()
    for segment in whisper_json['segments']:
        whisper_tree.addi(segment['start'], segment['end'], segment)

    # Iterate over the pyannote segments
    for pyannote_segment in pyannote_json['segments']:
        # Get the whisper segment that is closest to the pyannote segment
        whisper_transcript = get_whisper_transcript(whisper_tree, pyannote_segment)

        # Add the result to the dialog
        dialogs.append({'speaker': pyannote_segment['speaker'], 'start': pyannote_segment['start'],
                        'end': pyannote_segment['end'], 'text': whisper_transcript})

    return {'dialogs': dialogs, 'speakers': pyannote_json['speakers']}


def fuse_whisper_words_to_pyannote(whisper_json, pyannote_json):
    """
    Iterate over the whisper words and add them to the pyannote segments
    :param whisper_json: Loaded json file for whisper
    :param pyannote_json: Loaded json file for pyannote
    :return: Dictionary with the fused segments with speaker information
    """

    # These are the list of speakers from pyannote
    speakers = pyannote_json['speakers']

    # Iterate over the whisper segments and each word over it
    whisper_segments = whisper_json['segments']
    pyannote_segments = pyannote_json['segments']

    # Create a interval tree for the pyannote segments
    pyannote_tree = IntervalTree()
    for index, segment in enumerate(pyannote_segments):
        pyannote_tree.addi(segment['start'], segment['end'], (index, segment))

    # Create a empty list of dialogs of the same length as the pyannote segments
    dialogs = [
        {'speaker': speakers.index(segment['speaker']), 'start': segment['start'], 'end': segment['end'], 'text': ''}
        for segment in pyannote_segments]

    for segment in whisper_segments:
        for word in segment['words']:
            pyannote_segment = get_closest_intersection_segment(pyannote_tree, word)
            dialog_index = pyannote_segment.data[0]
            dialogs[dialog_index]['text'] += word['word']

    return {'dialogs': dialogs, 'speakers': pyannote_json['speakers']}


def run_whisper_on_segments(segments, audio_filename, HUGGING_FACE_API_KEY, hints=None, initial_prompt=None):
    """
    Run whisper on the segments
    :param segments: List of segments
    :param audio_filename: Audio filename that we are going re-run whisper on
    :param hints: Hints for whisper. If none, then no hints are used
    :param initial_prompt: Initial prompt to use for whisper
    :return: Whisper transcript
    """

    # Load whisper
    model = whisper.load_model("large-v2")
    audio = whisper.load_audio(audio_filename)

    # Load the model for voice activity detection
    pipeline = Pipeline.from_pretrained("pyannote/voice-activity-detection",
                                        use_auth_token=HUGGING_FACE_API_KEY)

    whisper_outputs = []

    # Run whisper on the segments
    for index, segment in enumerate(segments):
        audio_segment_start = int(WHISPER_SAMPLE_RATE * segment['start'])
        audio_segment_end = int(WHISPER_SAMPLE_RATE * segment['end'])
        segment_audio = audio[audio_segment_start:audio_segment_end]

        # Run voice activity detection on the segment
        audio_data = torch.tensor(np.row_stack((segment_audio, segment_audio)), dtype=torch.float32)
        output = pipeline({"waveform": audio_data, "sample_rate": WHISPER_SAMPLE_RATE})
        voice_activity_detection = output.get_timeline().support()

        # If there is no voice activity detected, then add a blank line
        if len(voice_activity_detection) == 0:
            whisper_outputs.append({'text': ''})
            continue

        if hints is not None:
            segment_output = model.transcribe(segment_audio, prompt=hints[index], word_timestamps=True)
        elif initial_prompt is not None:
            segment_output = model.transcribe(segment_audio, initial_prompt=initial_prompt, word_timestamps=True)
        else:
            segment_output = model.transcribe(segment_audio, word_timestamps=True)
        whisper_outputs.append(segment_output)

    return {'whisper_outputs': whisper_outputs}


def fuse_run_whisper_on_pyannote_segments(pyannote_json, audio_filename, pyannote_whisper_json_filename,
                                          HUGGING_FACE_API_KEY, initial_prompt=None):
    """
    For each pyannote segment, run whisper on the segment and add the result to the pyannote segment
    :param pyannote_json: Loaded json file for pyannote
    :param audio_filename: Audio filename that we are going re-run whisper on
    :param pyannote_whisper_json_filename: Filename to store the re-run of whisper on pyannote segments
    :param initial_prompt: Initial prompt to use for whisper
    :return: Dictionary with the fused segments with speaker information
    """

    # Speakers from pyannote
    speakers = pyannote_json['speakers']

    # Get the pyannote segments
    pyannote_segments = pyannote_json['segments']

    # Check if the file exists
    if not os.path.exists(pyannote_whisper_json_filename):
        # Load all the segments from pyannote
        whisper_outputs = run_whisper_on_segments(pyannote_segments, audio_filename, HUGGING_FACE_API_KEY)

        # Write the data to a json file
        with open(pyannote_whisper_json_filename, 'w') as f:
            json.dump(whisper_outputs, f, indent=2)
    else:
        # Load the json file
        with open(pyannote_whisper_json_filename, 'r') as f:
            whisper_outputs = json.load(f)

    # Iterate over the pyannote segments and use the text from the whisper_outputs to create the dialogs
    dialogs = []
    for index, segment in enumerate(pyannote_segments):
        whisper_second_output = whisper_outputs['whisper_outputs'][index]
        speaker_index = speakers.index(segment['speaker'])

        words = []
        # Make sure it has segments
        if 'segments' in whisper_second_output:
            for whisper_second_segment in whisper_second_output['segments']:
                words.extend(whisper_second_segment['words'])

        dialogs.append({'speaker': speaker_index, 'start': segment['start'], 'end': segment['end'],
                        'text': whisper_second_output['text'], 'words': words})

    return {'dialogs': dialogs, 'speakers': speakers}


def remove_punctuation_and_lowercase(sentence):
    """
    Remove punctuation and convert to lowercase
    :param sentence: Sentence to remove punctuation and convert to lowercase
    :return: Cleaned sentence
    """
    # Remove punctuation
    sentence_without_punctuation = ''.join([char for char in sentence if char not in string.punctuation])
    # Convert to lowercase
    return sentence_without_punctuation.lower()


def fuse_run_whisper_on_pyannote_segments_with_hints(whisper_json, pyannote_json, audio_filename,
                                                     pyannote_whisper_json_filename, HUGGING_FACE_API_KEY):
    """
    For each pyannote segment, run whisper on the segment and add the result to the pyannote segment and use the hints
    from the whisper_json to improve the results
    :param whisper_json: Loaded json file for whisper
    :param pyannote_json: Loaded json file for pyannote
    :param audio_filename:  Audio filename that we are going re-run whisper on
    :param pyannote_whisper_json_filename: Output filename to store the re-run of whisper on pyannote segments
    :return: Dictionary with the fused segments with speaker information
    """
    # Get the pyannote segments
    pyannote_segments = pyannote_json['segments']

    # Check if the file exists
    if not os.path.exists(pyannote_whisper_json_filename):
        # Create the interval tree for the whisper segments
        whisper_tree = IntervalTree()
        for segment in whisper_json['segments']:
            whisper_tree.addi(segment['start'], segment['end'], segment)

        # Load spacy
        nlp = spacy.load("en_core_web_sm")

        # Create the hints for the pyannote segments
        pyannote_hints = []
        for segment in pyannote_segments:
            whisper_segments = whisper_tree.overlap(segment['start'], segment['end'])
            interval_transcript = ''
            for whisper_segment in whisper_segments:
                interval_transcript += whisper_segment.data['text'] + ' '

            # Remove punctuations and convert to lowercase
            interval_transcript = remove_punctuation_and_lowercase(interval_transcript)

            # Remove the common words using spacy and keep only the important words
            interval_transcript = nlp(interval_transcript)
            interval_transcript = [token.text for token in interval_transcript if not token.is_stop]
            interval_transcript = ' '.join(interval_transcript)

            pyannote_hints.append(interval_transcript)

        # Load all the segments from pyannote
        whisper_outputs = run_whisper_on_segments(pyannote_segments, audio_filename, HUGGING_FACE_API_KEY,
                                                  pyannote_hints)

        # Write the data to a json file
        with open(pyannote_whisper_json_filename, 'w') as f:
            json.dump(whisper_outputs, f, indent=2)
    else:
        # Load the json file
        with open(pyannote_whisper_json_filename, 'r') as f:
            whisper_outputs = json.load(f)

    # Iterate over the pyannote segments and use the text from the whisper_outputs to create the dialogs
    dialogs = []
    for index, segment in enumerate(pyannote_segments):
        whisper_second_output = whisper_outputs['whisper_outputs'][index]
        dialogs.append({'speaker': segment['speaker'], 'start': segment['start'], 'end': segment['end'],
                        'text': whisper_second_output['text']})

    return {'dialogs': dialogs, 'speakers': pyannote_json['speakers']}


def fuse_word_corrections(whisper_json, transcript_json, n_words=250, logger=None, initial_prompt=None):
    """
    Fuse the word corrections from whisper to the transcript
    :param whisper_json: Whisper json file
    :param transcript_json: Transcript json file
    :param n_words: Number of words to fuse at a time
    :param logger: Logger to use for logging
    :param initial_prompt: Initial prompt from which we will only correct if given
    :return: Fused json file
    """

    # Remove the punctuation and convert to lowercase
    replace_chars = ",.?'`′-"
    trans = str.maketrans("", "", replace_chars)

    # Get the text from the whisper json
    whisper_text = whisper_json['text']
    whisper_text_clean = whisper_text.translate(trans).lower()
    whisper_words = whisper_text_clean.split()
    whisper_words_original = whisper_text.split()

    # Get the text from the transcript json
    dialogs_words = []
    for index, dialog in enumerate(transcript_json['dialogs']):
        dialog_text = dialog['text']
        dialog_text = dialog_text.translate(trans).lower()
        dialog_words = dialog_text.split()
        # Add the index to each of the dialog words to keep track of the which segment the word came from
        dialog_words_index = [(word, index, k) for k, word in enumerate(dialog_words)]
        dialogs_words.extend(dialog_words_index)

    # If there is initial prompt, create the list of words that are in the initial prompt
    initial_prompt_words = None
    if initial_prompt is not None:
        initial_prompt_clean = initial_prompt.translate(trans).lower()
        initial_prompt_words = initial_prompt_clean.split()

    # Iterate over the dialog words and replace the words from the whisper words.
    # We will step over n_words at a time
    dialogs_words_index = 0
    whisper_words_index = 0
    while dialogs_words_index < len(dialogs_words) and whisper_words_index < len(whisper_words):
        # Get the words to replace
        dialogs_words_to_replace = dialogs_words[dialogs_words_index:dialogs_words_index + n_words]
        dialogs_words_to_replace = [word for word, index, word_index in dialogs_words_to_replace]

        # Get the words to replace with
        whisper_words_to_replace = whisper_words[whisper_words_index:whisper_words_index + n_words]

        # Calculate the WER backtrace
        wer_result, S, N, operations = calc_wer_backtrace_words(dialogs_words_to_replace, whisper_words_to_replace)

        # Find the last word that is the same going backwards
        last_same_word_index = -1
        for index in reversed(range(len(operations))):
            operation = operations[index]
            if operation == ' ':
                last_same_word_index = index
                break

        if last_same_word_index == -1:
            # No same words. Replace all the words
            last_same_word_index = n_words

        # Replace the words
        k = 0
        j = 0
        for i in range(last_same_word_index):
            operation = operations[i]
            if operation == 'S':
                # Use metaphone to check if the words sound the same
                original_word = dialogs_words[dialogs_words_index + k][0]
                candidate_word = whisper_words[whisper_words_index + j]

                # If there is an initial prompt, then check if the word is in the initial prompt
                if initial_prompt_words is not None:
                    if candidate_word not in initial_prompt_words:
                        j += 1
                        k += 1
                        logger.info('Not in initial prompt: ' + candidate_word + ' -> ' + original_word)
                        continue

                # Only consider the words that are phonetically similar
                if jellyfish.metaphone(original_word) == jellyfish.metaphone(candidate_word):
                    original_whisper_word = whisper_words_original[whisper_words_index + j]
                    original_transcript_segment = dialogs_words[dialogs_words_index + k][1]
                    original_transcript_word_index = dialogs_words[dialogs_words_index + k][2]
                    segment_text = transcript_json['dialogs'][original_transcript_segment]['text']
                    original_transcript_word = segment_text.split()[original_transcript_word_index]

                    # Log the words that are being replaced
                    if logger is not None:
                        logger.info(original_transcript_word + ' -> ' + original_whisper_word)

                    # Replace the word
                    transcript_json['dialogs'][original_transcript_segment]['text'] = segment_text.replace(
                        original_transcript_word,
                        original_whisper_word)
                j += 1
                k += 1
            elif operation == 'D':
                k += 1
            elif operation == 'I':
                j += 1
            else:
                j += 1
                k += 1

        # If both j and k are 0, then there was no change and cannot continue
        if j == 0 and k == 0:
            break

        # Update the indexes
        dialogs_words_index += k
        whisper_words_index += j

    return transcript_json


def run_whisperx_alignment(whisper_json, audio_filename):
    """
    Take the whisper json and run the whisperx align on it to get precise word timings. Put the word timings on to
    pyannote segments.
    :param whisper_json: Whisper json data
    :param audio_filename: Audio file that we want the transcript for
    :return: Transcript data from whisperx alignment on pyannote segments and the alignment result
    """

    # Setup and run the whisperx model
    device = 'cuda'
    audio = whisperx.load_audio(audio_filename)
    model_a, metadata = whisperx.load_align_model(language_code=whisper_json["language"], device=device)
    alignment_result = whisperx.align(whisper_json["segments"], model_a, metadata, audio, device,
                                      return_char_alignments=False)

    return alignment_result


def whisperx_align(pyannote_json, whisperx_alignment_json):
    # Get the pyannote segments
    pyannote_segments = pyannote_json['segments']
    pyannote_speakers = pyannote_json['speakers']

    # Get the whisperx words (called word-segments)
    whisperx_words = whisperx_alignment_json['word_segments']

    # Add all the pyannote segments to the interval tree
    pyannote_segments_tree = IntervalTree()
    for segment in pyannote_segments:
        pyannote_segments_tree.addi(segment['start'], segment['end'], segment)

    # Create an array to hold the words for each pyannote segment
    for segment in pyannote_segments:
        segment['words'] = []

    # For each word, find the closest pyannote segment
    for word in whisperx_words:
        # Check that the word has a start and end time
        if 'start' not in word or 'end' not in word:
            continue
        pyannote_segment = get_closest_intersection_segment(pyannote_segments_tree, word)
        pyannote_segment.data['words'].append(word)

    # Iterate over the pyannote segments and use the text from the whisper_outputs to create the dialogs
    dialogs = []

    for index, segment in enumerate(pyannote_segments):
        dialog_words = []
        dialog = ''

        # Sort the list by start time
        relevant_words = segment['words']
        relevant_words.sort(key=lambda x: x['start'])

        # Add the intersection words in to the dialogs and dialog words
        for word in relevant_words:
            dialog += word['word'] + ' '
            dialog_words.append(word)

        speaker_index = pyannote_speakers.index(segment['speaker'])
        dialogs.append({'speaker': speaker_index, 'start': segment['start'], 'end': segment['end'],
                        'text': dialog, 'words': dialog_words})

    return {'dialogs': dialogs, 'speakers': pyannote_json['speakers']}
