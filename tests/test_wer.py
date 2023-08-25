from whisper_pyannote_fusion.wer import calc_wer, calc_wer_local, calc_wer_backtrace


def test_wer_subs():
    """
    Calculate the word error rate (WER) between two small sentences
    """
    reference = "hello world and duck"
    hypothesis = "hello duck and doku"

    error = calc_wer(reference, hypothesis)
    assert error == 0.5

    error2, s2, n2 = calc_wer_local(reference, hypothesis)
    assert error2 == 0.5


def test_wer_del():
    """
    Calculate the word error rate (WER) between two small sentences with a deletion
    """
    reference = "hello world and duck"
    hypothesis = "hello and duck"

    error = calc_wer(reference, hypothesis)
    assert error == 0.25

    error2, s2, n2 = calc_wer_local(reference, hypothesis)
    assert error2 == 0.25


#
def test_wer_ins():
    """
    Calculate the word error rate (WER) between two small sentences with an insertion
    """
    reference = "hello world and duck"
    hypothesis = "hello world and duck and doku"

    error = calc_wer(reference, hypothesis)
    assert error == 0.5

    error2, s2, n2 = calc_wer_local(reference, hypothesis)
    assert error2 == 0.5


def test_wer_with_backtrace():
    """
    Calculate the word error rate (WER) between two small sentences and check the sequence of operations
    """

    # Two substitutions
    reference = "hello world and duck"
    hypothesis = "hello duck and doku"

    error, S, N, operations = calc_wer_backtrace(reference, hypothesis)
    assert error == 0.5
    assert operations == [' ', 'S', ' ', 'S']

    # One deletion
    reference = "hello world and duck"
    hypothesis = "hello and duck"

    error, S, N, operations = calc_wer_backtrace(reference, hypothesis)
    assert error == 0.25
    assert operations == [' ', 'D', ' ', ' ']

    # One insertion
    reference = "hello world and duck"
    hypothesis = "hello world and duck and doku"

    error, S, N, operations = calc_wer_backtrace(reference, hypothesis)
    assert error == 0.5
    assert operations == [' ', ' ', ' ', ' ', 'I', 'I']

