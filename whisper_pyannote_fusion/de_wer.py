from intervaltree import IntervalTree
from whisper_normalizer.english import EnglishTextNormalizer

from .interval_utils import get_largest_intersection_segment
from .wer import calc_wer_local, calc_wer_backtrace


def calc_de_wer(reference_json, hypothesis_json, print_errors=False, normalize=False, ignore_length=3):
    """
    Calculate the WER on segments that match up. If no segment matches up, then the word error rate is 100%.
    :param reference_json: Reference JSON file read in as dictionary
    :param hypothesis_json: Hypothesis JSON file read in as dictionary
    :param print_errors: Print the errors
    :param normalize: Normalize the WER by the number of words in the reference
    :return: DE-WER
    """

    # Put all the hypothesis segments into an interval tree
    hypothesis_tree = IntervalTree()
    for segment in hypothesis_json['dialogs']:
        hypothesis_tree.addi(segment['start'], segment['end'], segment)

    # Iterate over the reference segments
    total_words = 0
    total_errors = 0
    for reference_segment in reference_json['dialogs']:
        # Check that the reference segment has is at least a second long and has at least four words
        if len(reference_segment['text'].split()) < ignore_length:
            continue

        # Get the hypothesis segment that is closest to the reference segment
        hypothesis_segment = get_largest_intersection_segment(hypothesis_tree, reference_segment)

        # Get the reference and hypothesis strings
        reference_str = reference_segment['text']

        # If there is no hypothesis segment, then the WER is 100%
        if hypothesis_segment is None:
            total_words += len(reference_str.split())
            total_errors += len(reference_str.split())
            continue

        hypothesis_str = hypothesis_segment.data['text']

        if normalize:
            normalizer = EnglishTextNormalizer()
            reference_str = normalizer(reference_str)
            hypothesis_str = normalizer(hypothesis_str)

        # Calculate the WER
        if print_errors:
            wer, errors, words, operations = calc_wer_backtrace(reference_str, hypothesis_str)
            reference_words = reference_str.split()
            hypothesis_words = hypothesis_str.split()

            has_error = False
            for operation in operations:
                if operation == ' ':
                    # print(reference_words[0], end=' ')
                    reference_words = reference_words[1:]
                    hypothesis_words = hypothesis_words[1:]
                elif operation == 'S':
                    print(reference_words[0] + '/' + hypothesis_words[0], end=' ')
                    reference_words = reference_words[1:]
                    hypothesis_words = hypothesis_words[1:]
                    has_error = True
                elif operation == 'D':
                    print('-' + reference_words[0], end=' ')
                    reference_words = reference_words[1:]
                    has_error = True
                elif operation == 'I':
                    print('+' + hypothesis_words[0], end=' ')
                    hypothesis_words = hypothesis_words[1:]
                    has_error = True
            if has_error:
                print()
        else:
            wer, errors, words = calc_wer_local(reference_str, hypothesis_str)

        if errors > words:
            errors = words

        # Update the total words and errors
        total_words += words
        total_errors += errors

    # Calculate the WER
    # If total words is 0, the wer is NaN
    if total_words == 0:
        wer = float('nan')
    else:
        wer = total_errors / total_words

    return wer
