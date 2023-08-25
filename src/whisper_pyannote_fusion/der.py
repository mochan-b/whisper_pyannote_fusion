from pyannote.core import Segment, Annotation
from pyannote.metrics.diarization import DiarizationErrorRate


# Calculate the diarization error rate (DER) using pyannote.metrics library
def calc_der(reference_data, hypothesis_data):
    # Convert the reference and hypothesis to pyannote.core.Annotation objects
    reference = Annotation(uri='reference')
    for interval, speaker in reference_data:
        reference[Segment(interval[0], interval[1])] = speaker
    hypothesis = Annotation(uri='hypothesis')
    for interval, speaker in hypothesis_data:
        hypothesis[Segment(interval[0], interval[1])] = speaker

    return DiarizationErrorRate()(reference, hypothesis)
