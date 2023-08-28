import json
from whisper_normalizer.english import EnglishTextNormalizer

from whisper_pyannote_fusion.wer import calc_wer
from whisper_pyannote_fusion.der import calc_der
from whisper_pyannote_fusion.de_wer import calc_de_wer


# Open the JSON file for the ground truth data and get the reference string
def get_transcript_string(ground_truth_json):
    # Open the json file
    with open(ground_truth_json, 'r') as f:
        data = json.load(f)

    # Get the reference string
    reference = ''
    for dialog in data['dialogs']:
        reference += dialog['text'] + ' '

    return reference


# Open the JSON file for the whisper transcript and get the string
def get_whisper_string(whisper_json):
    # Open the json file
    with open(whisper_json, 'r') as f:
        data = json.load(f)

    return data['text']


def calculate_wer(ground_truth_data, whisper_transcript):
    reference_str = get_transcript_string(ground_truth_data)
    hypothesis_str = get_whisper_string(whisper_transcript)

    wer = calc_wer(reference_str, hypothesis_str)

    normalizer = EnglishTextNormalizer()
    reference_str = normalizer(reference_str)
    hypothesis_str = normalizer(hypothesis_str)
    wer_normalized = calc_wer(reference_str, hypothesis_str)

    return wer, wer_normalized


def calculate_wer_comparison(ground_truth_data, fusion_method1):
    reference_str = get_transcript_string(ground_truth_data)
    fusion_str = get_transcript_string(fusion_method1)

    wer = calc_wer(reference_str, fusion_str)

    normalizer = EnglishTextNormalizer()
    reference_str = normalizer(reference_str)
    fusion_str = normalizer(fusion_str)
    wer_normalized = calc_wer(reference_str, fusion_str)

    return wer, wer_normalized


def get_transcript_intervals(ground_truth_data):
    # Open the json file
    with open(ground_truth_data, 'r') as f:
        data = json.load(f)

    # Get the reference string
    reference_intervals = []
    for dialog in data['dialogs']:
        reference_intervals.append(((dialog['start'], dialog['end']), str(dialog['speaker'])))

    return reference_intervals


def get_pyannot_intervals(pyannote_result):
    # Open the json file
    with open(pyannote_result, 'r') as f:
        data = json.load(f)

    # Get the reference string
    pyannote_intervals = []
    for dialog in data['segments']:
        speaker_index = data['speakers'].index(dialog['speaker'])
        pyannote_intervals.append(((dialog['start'], dialog['end']), str(speaker_index)))

    return pyannote_intervals


def calculate_der(ground_truth_data, pyannote_result):
    reference_intervals = get_transcript_intervals(ground_truth_data)
    pyannote_intervals = get_pyannot_intervals(pyannote_result)
    return calc_der(reference_intervals, pyannote_intervals)


def calculate_der_comparison(ground_truth_data, fusion_method):
    reference_intervals = get_transcript_intervals(ground_truth_data)
    fuse_intervals = get_transcript_intervals(fusion_method)
    return calc_der(reference_intervals, fuse_intervals)


def calculate_de_wer(ground_truth_data, fusion_method):
    """
    Calculate the DE-WER between the ground truth and the fusion method
    :param ground_truth_data: Ground truth data
    :param fusion_method: Fusion method
    :return: DE-WER
    """
    # Open the json file
    with open(ground_truth_data, 'r') as f:
        reference_json = json.load(f)

    # Open the json file
    with open(fusion_method, 'r') as f:
        hypothesis_json = json.load(f)

    return calc_de_wer(reference_json, hypothesis_json, normalize=True)


def calculate_de_wer_print_errors(ground_truth_data, fusion_method):
    """
    Calculate the DE-WER between the ground truth and the fusion method
    :param ground_truth_data: Ground truth data
    :param fusion_method: Fusion method
    :return: DE-WER
    """
    # Open the json file
    with open(ground_truth_data, 'r') as f:
        reference_json = json.load(f)

    # Open the json file
    with open(fusion_method, 'r') as f:
        hypothesis_json = json.load(f)

    return calc_de_wer(reference_json, hypothesis_json, print_errors=True, normalize=True)


if __name__ == '__main__':
    print('----- Analysis of transcripts -----')

    # The analysis that we will be doing on the transcripts
    fusion_methods = {4, 4.1, 4.2, 5, 6, 7}

    ground_truth_data = '../data/gt_marti_john.json'
    whisper_transcript = '../data/whisper_transcript.json'
    pyannote_result = '../data/pyannote_results.json'

    # Calculate the metrics for whisper
    if 0 in fusion_methods:
        wer, wer_normalized = calculate_wer(ground_truth_data, whisper_transcript)
        print('WER between ground truth vs Whisper output: ', wer)
        print('WER between ground truth vs Whisper output (normalized): ', wer_normalized)

        der = calculate_der(ground_truth_data, pyannote_result)
        print('DER between ground truth vs PyAnnote output: ', der)

    # Calculate the metrics for fusion method 1
    if 1 in fusion_methods:
        print('----- Analysis of fusion method 1 -----')
        fusion_method1 = '../data/whisper_pyannote_fuse_method1.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method1)
        print('WER between ground truth vs Fusion method 1 output: ', wer)
        print('WER between ground truth vs Fusion method 1 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method1)
        print('DER between ground truth vs Fusion method 1 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method1)
        print('DE-WER between ground truth vs Fusion method 1 output: ', we_der)

    # Calculate the metrics for fusion method 2
    if 2 in fusion_methods:
        print('----- Analysis of fusion method 2 -----')

        fusion_method2 = '../data/whisper_pyannote_fuse_method2.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method2)
        print('WER between ground truth vs Fusion method 2 output: ', wer)
        print('WER between ground truth vs Fusion method 2 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method2)
        print('DER between ground truth vs Fusion method 2 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method2)
        print('DE-WER between ground truth vs Fusion method 1 output: ', we_der)

    # Calculate the metrics for fusion method 3
    if 3 in fusion_methods:
        print('----- Analysis of fusion method 3 -----')

        fusion_method3 = '../data/whisper_pyannote_fuse_method3.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method3)
        print('WER between ground truth vs Fusion method 3 output: ', wer)
        print('WER between ground truth vs Fusion method 3 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method3)
        print('DER between ground truth vs Fusion method 3 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method3)
        print('DE-WER between ground truth vs Fusion method 3 output: ', we_der)

    # Calculate the metrics for fusion method 4
    if 4 in fusion_methods:
        print('----- Analysis of fusion method 4 -----')

        fusion_method4 = '../data/whisper_pyannote_fuse_method4.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method4)
        print('WER between ground truth vs Fusion method 4 output: ', wer)
        print('WER between ground truth vs Fusion method 4 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method4)
        print('DER between ground truth vs Fusion method 4 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method4)
        print('DE-WER between ground truth vs Fusion method 4 output: ', we_der)

    # Calculate the metrics for fusion method 4.1
    if 4.1 in fusion_methods:
        print('----- Analysis of fusion method 4.1 -----')

        fusion_method4_1 = '../data/whisper_pyannote_fuse_method4_1.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method4_1)
        print('WER between ground truth vs Fusion method 4.1 output: ', wer)
        print('WER between ground truth vs Fusion method 4.1 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method4_1)
        print('DER between ground truth vs Fusion method 4.1 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method4_1)
        print('DE-WER between ground truth vs Fusion method 4.1 output: ', we_der)

        # Calculate we_dir and also print out the errors
        # calculate_de_wer_print_errors(ground_truth_data, fusion_method4_1)

    # Calculate the metrics for fusion method 4.2
    if 4.2 in fusion_methods:
        print('----- Analysis of fusion method 4.2 -----')

        fusion_method4_2 = '../data/whisper_pyannote_fuse_method4_2.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method4_2)
        print('WER between ground truth vs Fusion method 4.2 output: ', wer)
        print('WER between ground truth vs Fusion method 4.2 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method4_2)
        print('DER between ground truth vs Fusion method 4.2 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method4_2)
        print('DE-WER between ground truth vs Fusion method 4.2 output: ', we_der)

        # Calculate we_dir and also print out the errors
        # calculate_de_wer_print_errors(ground_truth_data, fusion_method4_2)

    # Calculate the metrics for fusion method 5
    if 5 in fusion_methods:
        print('----- Analysis of fusion method 5 -----')

        fusion_method5 = '../data/whisper_pyannote_fuse_method5.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method5)
        print('WER between ground truth vs Fusion method 5 output: ', wer)
        print('WER between ground truth vs Fusion method 5 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method5)
        print('DER between ground truth vs Fusion method 5 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method5)
        print('DE-WER between ground truth vs Fusion method 5 output: ', we_der)

    # Calculate the metrics for fusion method 6 : substitute the transcript words with whisper words
    if 6 in fusion_methods:
        print('----- Analysis of fusion method 6 -----')

        fusion_method6 = '../data/whisper_pyannote_fuse_method6.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method6)
        print('WER between ground truth vs Fusion method 6 output: ', wer)
        print('WER between ground truth vs Fusion method 6 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method6)
        print('DER between ground truth vs Fusion method 6 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method6)
        print('DE-WER between ground truth vs Fusion method 6 output: ', we_der)

    # Calculate the metrics for fusion method 7 : use whisper-x to align the transcript words with whisper words
    if 7 in fusion_methods:
        print('----- Analysis of fusion method 7 -----')

        fusion_method7 = '../data/whisper_pyannote_fuse_method7.json'
        wer, wer_normalized = calculate_wer_comparison(ground_truth_data, fusion_method7)
        print('WER between ground truth vs Fusion method 7 output: ', wer)
        print('WER between ground truth vs Fusion method 7 output (normalized): ', wer_normalized)

        der = calculate_der_comparison(ground_truth_data, fusion_method7)
        print('DER between ground truth vs Fusion method 7 output: ', der)

        we_der = calculate_de_wer(ground_truth_data, fusion_method7)
        print('DE-WER between ground truth vs Fusion method 7 output: ', we_der)