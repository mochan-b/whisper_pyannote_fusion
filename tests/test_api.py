import json
import os

from whisper_pyannote_fusion.fusion_methods import fuse_add_speaker_to_whisper_segments, \
    fuse_add_transcript_to_pyannote_segments, \
    fuse_whisper_words_to_pyannote, fuse_run_whisper_on_pyannote_segments, \
    fuse_word_corrections, run_whisperx_alignment
from whisper_pyannote_fusion import whisper_pyannote_fusion

data_dir_name = '../data/'

HUGGING_FACE_API_KEY = "hf_invalid_key"


def get_whisper_pyannote_json_files():
    whisper_json_filename = os.path.join(data_dir_name, 'whisper_transcript.json')
    pyannote_json_filename = os.path.join(data_dir_name, 'pyannote_results.json')
    return whisper_json_filename, pyannote_json_filename


def get_whisper_pyannote_json():
    # Name of the json files
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()

    # Read the json files
    with open(whisper_json_filename, 'r') as f:
        whisper_json = json.load(f)
    with open(pyannote_json_filename, 'r') as f:
        pyannote_json = json.load(f)

    return whisper_json, pyannote_json


def test_pyannote_to_whisper():
    """
    Test the pyannote to whisper segments fusion method
    """
    whisper_json, pyannote_json = get_whisper_pyannote_json()

    result = fuse_add_speaker_to_whisper_segments(whisper_json, pyannote_json)
    assert result is not None
    assert len(result['dialogs']) == 446


def test_pyannote_to_whisper_api():
    """
    Test the pyannote to whisper segments fusion method
    """
    audio_filename = os.path.join(data_dir_name, '626.mp3')
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()
    result = whisper_pyannote_fusion(audio_filename, 'pyannote_to_whisper', whisper_json_filename,
                                     pyannote_json_filename)
    assert len(result['dialogs']) == 446


def test_whisper_to_pyannote():
    """
    Test the whisper to pyannote segments fusion method
    """
    whisper_json, pyannote_json = get_whisper_pyannote_json()

    result = fuse_add_transcript_to_pyannote_segments(whisper_json, pyannote_json)
    assert result is not None
    assert len(result['dialogs']) == 102


def test_whisper_to_pyannote_api():
    """
    Test the whisper to pyannote segments fusion method using the API
    """
    audio_filename = os.path.join(data_dir_name, '626.mp3')
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()
    result = whisper_pyannote_fusion(audio_filename, 'whisper_to_pyannote', whisper_json_filename,
                                     pyannote_json_filename)
    assert len(result['dialogs']) == 102


def test_whisper_words_to_pyannote():
    """
    Test the whisper words to pyannote segments fusion method
    """
    whisper_json, pyannote_json = get_whisper_pyannote_json()

    result = fuse_whisper_words_to_pyannote(whisper_json, pyannote_json)
    assert result is not None
    assert len(result['dialogs']) == 102


def test_whisper_words_to_pyannote_api():
    """
    Test the whisper words to pyannote segments fusion method using the API
    """
    audio_filename = os.path.join(data_dir_name, '626.mp3')
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()
    result = whisper_pyannote_fusion(audio_filename, 'whisper_words_to_pyannote', whisper_json_filename,
                                     pyannote_json_filename)
    assert len(result['dialogs']) == 102


def test_pyannote_segment_run_whisper():
    """
    Test the pyannote segment run whisper segments fusion method
    """
    whisper_json, pyannote_json = get_whisper_pyannote_json()
    whisper_pyannote_result_filename = os.path.join(data_dir_name, 'whisper_pyannote_results_1.json')
    result = fuse_run_whisper_on_pyannote_segments(pyannote_json, None, whisper_pyannote_result_filename,
                                                   HUGGING_FACE_API_KEY)
    assert result is not None
    assert len(result['dialogs']) == 102


def test_pyannote_segment_run_whisper_api():
    """
    Test the pyannote segment run whisper segments fusion method
    """
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()
    whisper_pyannote_result_filename = os.path.join(data_dir_name, 'whisper_pyannote_results_1_1.json')
    result = whisper_pyannote_fusion(None, 'whisper_words_to_pyannote', whisper_json_filename,
                                     pyannote_json_filename,
                                     pyannote_whisper_json_filename=whisper_pyannote_result_filename)
    assert result is not None
    assert len(result['dialogs']) == 102


def test_correct_pyannote_with_whisper():
    """
    Corrct pyannote with whisper segments fusion method
    """
    whisper_json, pyannote_json = get_whisper_pyannote_json()
    whisper_pyannote_result_filename = os.path.join(data_dir_name, 'whisper_pyannote_results_1.json')

    result_json = fuse_run_whisper_on_pyannote_segments(pyannote_json, None, whisper_pyannote_result_filename,
                                                        HUGGING_FACE_API_KEY)
    corrected_json = fuse_word_corrections(whisper_json, result_json, logger=None)

    assert corrected_json is not None
    assert len(corrected_json['dialogs']) == 102


def test_correct_pyannote_with_whisper_api():
    """
    Corrct pyannote with whisper segments fusion method using the api
    """
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()
    whisper_pyannote_result_filename = os.path.join(data_dir_name, 'whisper_pyannote_results_1.json')

    corrected_json = whisper_pyannote_fusion(None, 'correct_pyannote_with_whisper', whisper_json_filename,
                                             pyannote_json_filename,
                                             pyannote_whisper_json_filename=whisper_pyannote_result_filename,
                                             HUGGING_FACE_API_KEY=HUGGING_FACE_API_KEY)

    assert corrected_json is not None
    assert len(corrected_json['dialogs']) == 102


def test_whisperx_align_pyannote():
    """
    Test the whisperx align pyannote segments fusion method
    """
    audio_filename = os.path.join(data_dir_name, '626.mp3')
    whisper_json_filename, pyannote_json_filename = get_whisper_pyannote_json_files()
    whisperx_alignment_json_filename = os.path.join(data_dir_name, 'whisperx_alignment.json')
    final_data = whisper_pyannote_fusion(audio_file=audio_filename, method='whisperx_align_pyannote',
                                         whisper_json_file=whisper_json_filename,
                                         pyannote_json_file=pyannote_json_filename,
                                         whisperx_alignment_json_filename=whisperx_alignment_json_filename)

    assert final_data is not None
    assert len(final_data['dialogs']) == 102
