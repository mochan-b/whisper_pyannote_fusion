from whisper_pyannote_fusion.de_wer import calc_de_wer


def test_de_wer_calc():
    """
    Test the DE-WER calculation by creating a reference and hypothesis JSON file and comparing the result to the
    expected result.
    """
    reference_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello'},
                                   {'start': 1, 'end': 2, 'text': 'world'}]}
    hypothesis_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello'},
                                    {'start': 1, 'end': 2, 'text': 'world'}]}
    de_wer = calc_de_wer(reference_json, hypothesis_json, ignore_length=0)
    assert de_wer == 0

    reference_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello'},
                                   {'start': 1, 'end': 2, 'text': 'world'}]}
    hypothesis_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello'},
                                    {'start': 1, 'end': 2, 'text': 'world'},
                                    {'start': 2, 'end': 3, 'text': '!'}]}
    de_wer = calc_de_wer(reference_json, hypothesis_json, ignore_length=0)
    assert de_wer == 0

    reference_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello'},
                                   {'start': 1, 'end': 2, 'text': 'world'},
                                   {'start': 2, 'end': 3, 'text': '!'},
                                   {'start': 3, 'end': 4, 'text': '!'}]}
    hypothesis_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello'},
                                    {'start': 1, 'end': 2, 'text': 'world'}]}
    de_wer = calc_de_wer(reference_json, hypothesis_json, ignore_length=0)
    assert de_wer == 0.5

    reference_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello world hola mundo'},
                                   {'start': 1, 'end': 2, 'text': '!'}]}
    hypothesis_json = {'dialogs': [{'start': 0, 'end': 1, 'text': 'hello world'},
                                    {'start': 1, 'end': 2, 'text': 'hola mundo'}]}
    de_wer = calc_de_wer(reference_json, hypothesis_json, ignore_length=0)
    assert de_wer == 0.6
