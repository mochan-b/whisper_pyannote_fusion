from whisper_pyannote_fusion.der import calc_der


# Test the DER of intervals and speakers associated with the intervals
def test_der():
    reference = [((0, 10), '0'), ((12, 20), '1'), ((24, 27), '0'), ((30, 40), '2')]
    hypothesis = [((2, 13), '0'), ((13, 14), '3'), ((14, 20), '1'), ((22, 38), '2'), ((38, 40), '3')]
    der_error = calc_der(reference, hypothesis)
    assert der_error == 0.5161290322580645
