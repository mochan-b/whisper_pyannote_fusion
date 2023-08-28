from jiwer import wer


# Calculate the word error rate (WER) between two sentences using the jiwer library
def calc_wer(reference, hypothesis):
    return wer(reference, hypothesis)


def calc_wer_local(reference, hypothesis):
    """
    Calculate the word error rate (WER) between two sentences using the local implementation
    :param reference: Reference sentence
    :param hypothesis: Hypothesis sentence
    :return: WER
    """
    # Tokenize the reference and hypothesis
    reference = reference.split()
    hypothesis = hypothesis.split()

    # Initialize the matrix
    matrix = [[0 for x in range(len(hypothesis) + 1)] for y in range(len(reference) + 1)]

    # Fill the first row and column
    for i in range(len(reference) + 1):
        matrix[i][0] = i
    for j in range(len(hypothesis) + 1):
        matrix[0][j] = j

    # Calculate the costs using dynamic programming
    for i in range(1, len(reference) + 1):
        for j in range(1, len(hypothesis) + 1):
            if reference[i - 1] == hypothesis[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1,  # Deletion
                               matrix[i][j - 1] + 1,  # Insertion
                               matrix[i - 1][j - 1] + substitution_cost)  # Substitution

    # Calculate WER
    s = matrix[len(reference)][len(hypothesis)]
    n = len(reference)
    wer_result = s / n

    return wer_result, s, n


def calc_wer_backtrace(reference, hypothesis):
    """
    Split the words and call calc_wer_backtrace_words
    :param reference: Reference sentence
    :param hypothesis: Hypothesis sentence
    :return: WER, sequence of operations (' ', 'S', 'D', 'I') where ' ' means same, 'S' means substitution, 'D' means
    deletion and 'I' means insertion
    """
    # Tokenize the reference and hypothesis
    reference = reference.split()
    hypothesis = hypothesis.split()

    return calc_wer_backtrace_words(reference, hypothesis)


def calc_wer_backtrace_words(reference, hypothesis):
    """
    Calculate the word error rate (WER) between two sentences using the local implementation with backtrace and return
    the sequence of operations to make the hypothesis sentence equal to the reference sentence
    :param reference: Reference sentence
    :param hypothesis: Hypothesis sentence
    :return: WER, sequence of operations (' ', 'S', 'D', 'I') where ' ' means same, 'S' means substitution, 'D' means
    """

    # Initialize the cost and backtrace matrices
    matrix = [[0 for x in range(len(hypothesis) + 1)] for y in range(len(reference) + 1)]
    backtrace = [["" for x in range(len(hypothesis) + 1)] for y in range(len(reference) + 1)]

    # Fill the first row and column
    for i in range(len(reference) + 1):
        matrix[i][0] = i
        backtrace[i][0] = "D"
    for j in range(len(hypothesis) + 1):
        matrix[0][j] = j
        backtrace[0][j] = "I"

    backtrace[0][0] = "S"  # Start

    # Calculate the costs and backtrace using dynamic programming
    for i in range(1, len(reference) + 1):
        for j in range(1, len(hypothesis) + 1):
            if reference[i - 1] == hypothesis[j - 1]:
                substitution_cost = 0
                operation = " "  # Same
            else:
                substitution_cost = 1
                operation = "S"  # Substitution

            costs = [matrix[i - 1][j] + 1,  # Deletion
                     matrix[i][j - 1] + 1,  # Insertion
                     matrix[i - 1][j - 1] + substitution_cost]  # Substitution

            matrix[i][j] = min(costs)
            backtrace[i][j] = ["D", "I", operation][costs.index(matrix[i][j])]

    # Reconstruct the sequence of operations
    i, j = len(reference), len(hypothesis)
    operations = []
    while i > 0 or j > 0:
        operation = backtrace[i][j]
        operations.append(operation)
        if operation == "S" or operation == " ":
            i -= 1
            j -= 1
        elif operation == "D":
            i -= 1
        elif operation == "I":
            j -= 1

    operations.reverse()

    # Calculate WER
    S, D, I = matrix[len(reference)][len(hypothesis)], matrix[len(reference)][0], matrix[0][len(hypothesis)]
    N = len(reference)
    wer_result = S / N

    return wer_result, S, N, operations
