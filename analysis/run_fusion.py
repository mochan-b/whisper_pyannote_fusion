import json
import logging
import os.path

from whisper_pyannote_fusion import transcript_to_workdown
from whisper_pyannote_fusion.fusion_methods import fuse_add_speaker_to_whisper_segments, \
    fuse_add_transcript_to_pyannote_segments, \
    fuse_whisper_words_to_pyannote, fuse_run_whisper_on_pyannote_segments, \
    fuse_run_whisper_on_pyannote_segments_with_hints, fuse_word_corrections, run_whisperx_alignment, whisperx_align
from config import HUGGING_FACE_API_KEY


def main(data_dir):
    # Global constants
    podcast_mp3_filename = os.path.join(data_dir, '626.mp3')

    # Configure logging
    logger = logging.getLogger('fusion_logger')
    logger.setLevel(level=logging.INFO)

    # Create a handler for outputting log messages to a stream
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add a file handler for outputting log messages to a file
    file_handler = logging.FileHandler(os.path.join(data_dir, 'fusion.log'))
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    # Load the json file for whisper and pyannote
    with open(os.path.join(data_dir, "whisper_transcript.json"), "r") as f:
        whisper_result = json.load(f)
    with open(os.path.join(data_dir, "pyannote_results.json"), "r") as f:
        pyannote_result = json.load(f)

    # Specify which fusion methods to generate files for
    fusion_methods = {6}

    # Fuse the data and get the transcript output
    if 1 in fusion_methods:
        fused_result = fuse_add_speaker_to_whisper_segments(whisper_result, pyannote_result)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method1.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 2 in fusion_methods:
        # Fuse the data and get the transcript output
        fused_result = fuse_add_transcript_to_pyannote_segments(whisper_result, pyannote_result)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method2.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 3 in fusion_methods:
        # Fuse the data and get the transcript output
        fused_result = fuse_whisper_words_to_pyannote(whisper_result, pyannote_result)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method3.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 4 in fusion_methods:
        # File where the re-run of whisper is stored as
        pyannote_whisper_json_filename_11 = os.path.join(data_dir, 'whisper_pyannote_results_1.json')

        # Fuse the data and get the transcript output
        fused_result = fuse_run_whisper_on_pyannote_segments(pyannote_result, podcast_mp3_filename,
                                                             pyannote_whisper_json_filename_11,
                                                             HUGGING_FACE_API_KEY=HUGGING_FACE_API_KEY)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method4.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 4.1 in fusion_methods:
        # File where the re-run of whisper is stored as
        pyannote_whisper_json_filename_11 = os.path.join(data_dir, 'whisper_pyannote_results_1_1.json')

        # Read the summary of the podcast and use that as the initial prompt
        prompt_file = os.path.join(data_dir, 'summary.txt')
        with open(prompt_file, 'r') as f:
            prompt = f.read()

        # Fuse the data and get the transcript output
        fused_result = fuse_run_whisper_on_pyannote_segments(pyannote_result, podcast_mp3_filename,
                                                             pyannote_whisper_json_filename_11,
                                                             initial_prompt=prompt,
                                                             HUGGING_FACE_API_KEY=HUGGING_FACE_API_KEY)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method4_1.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 4.2 in fusion_methods:
        # File where the re-run of whisper is stored as
        pyannote_whisper_json_filename_11 = os.path.join(data_dir, 'whisper_pyannote_results_1_1.json')

        # Read the summary of the podcast and use that as the initial prompt
        prompt_file = os.path.join(data_dir, 'prompt.txt')
        with open(prompt_file, 'r') as f:
            prompt = f.read()

        # Fuse the data and get the transcript output
        fused_result = fuse_run_whisper_on_pyannote_segments(pyannote_result, podcast_mp3_filename,
                                                             pyannote_whisper_json_filename_11,
                                                             initial_prompt=prompt,
                                                             HUGGING_FACE_API_KEY=HUGGING_FACE_API_KEY)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method4_2.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 5 in fusion_methods:
        # File where the re-run of whisper is stored as
        pyannote_whisper_json_filename_2 = os.path.join(data_dir, 'whisper_pyannote_results_2.json')

        # Fuse the data and get the transcript output
        fused_result = fuse_run_whisper_on_pyannote_segments_with_hints(whisper_result, pyannote_result,
                                                                        podcast_mp3_filename,
                                                                        pyannote_whisper_json_filename_2)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method5.json"), "w") as f:
            json.dump(fused_result, f, indent=2)

    if 6 in fusion_methods:
        # Previous file that was fused
        previous_fused_json_filename = os.path.join(data_dir, 'whisper_pyannote_fuse_method4.json')
        with open(previous_fused_json_filename, 'r') as f:
            fused_result = json.load(f)

        # Fuse the data and get the transcript output
        fused_result_fixed = fuse_word_corrections(whisper_result, fused_result, logger=logger)

        # Write the file as json to data folder as whisper_pyannote_fuse_method1.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method6.json"), "w") as f:
            json.dump(fused_result_fixed, f, indent=2)

    if 7 in fusion_methods:
        # Create the whisper-x alignment data
        whisperx_alignment_json_filename = os.path.join(data_dir, 'whisperx_alignment.json')
        if not os.path.exists(whisperx_alignment_json_filename):
            whisperx_alignment_json = run_whisperx_alignment(whisper_json=whisper_result,
                                                             audio_filename=podcast_mp3_filename)
            with open(whisperx_alignment_json_filename, 'w') as f:
                json.dump(whisperx_alignment_json, f, indent=2)
        else:
            with open(whisperx_alignment_json_filename, 'r') as f:
                whisperx_alignment_json = json.load(f)

        # Fuse the data and get the transcript output
        transcript_data = whisperx_align(pyannote_result, whisperx_alignment_json)

        # Write the file as json to data folder as whisper_pyannote_fuse_method7.json
        with open(os.path.join(data_dir, "whisper_pyannote_fuse_method7.json"), "w") as f:
            json.dump(transcript_data, f, indent=2)

        # Create the markdown file
        md_file = os.path.join(data_dir, 'whisper_pyannote_fuse_method7.md')
        transcript_to_workdown(transcript_data, md_file)


if __name__ == '__main__':
    directory_name = '../data/'
    main(directory_name)
