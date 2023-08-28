from intervaltree import Interval, IntervalTree


def intersection_length(interval1, interval2):
    """
    Calculate the length of the intersection between two intervals
    :param interval1: Interval 1
    :param interval2: Interval 2
    :return: Length of the intersection
    """
    return max(0, min(interval1[1], interval2[1]) - max(interval1[0], interval2[0]))


def get_largest_intersection_segment(tree, segment):
    """
    Get the segment from the tree that has the largest intersection with the given segment
    :param tree: Interval tree
    :param segment: Segment
    :return: Segment with the largest intersection
    """
    interval = Interval(segment['start'], segment['end'])

    # Find all the intersecting segments
    intersecting_segments = list(tree.overlap(interval))

    # If there are no intersecting segments, return None
    if len(intersecting_segments) == 0:
        return None

    # Get the size of the intersection for each interesting segment
    intersecting_segments_lengths = [intersection_length(segment, interval) for segment in intersecting_segments]

    # Check if there are multiple max values
    max_value = max(intersecting_segments_lengths)
    max_count = intersecting_segments_lengths.count(max_value)
    if max_count > 1:
        # If there are multiple max values, then return the segment that is closest to the given segment
        segment_lengths = [segment['end'] - segment['start'] for segment['data'] in intersecting_segments]
        min_index = segment_lengths.index(min(segment_lengths))
        return intersecting_segments[min_index]

    # Get the index of the segment with the largest intersection
    max_index = intersecting_segments_lengths.index(max(intersecting_segments_lengths))

    # Get the segment with the largest intersection
    segment = intersecting_segments[max_index]

    return segment


def calc_interval_distance(interval1, interval2):
    A1 = interval1[0]
    A2 = interval1[1]
    B1 = interval2[0]
    B2 = interval2[1]
    if A2 < B1:
        return B1 - A2
    elif B2 < A1:
        return A1 - B2
    else:
        return 0


def get_closest_intersection_segment(tree, segment):
    """
    Get the segment from the tree that has the largest intersection with the given segment. If there is no intersection,
    then return the closest segment.
    :param tree: Interval tree
    :param segment: Segment
    :return: Segment with the largest intersection or closest segment
    """
    best_segment = get_largest_intersection_segment(tree, segment)
    if best_segment is None:
        # Calculate the distance to each interval in the interval tree
        interval = Interval(segment['start'], segment['end'])

        tree_list = list(tree)
        interval_distances = [calc_interval_distance(interval, interval2) for interval2 in tree_list]

        # Get the interval with the smallest distance
        min_index = interval_distances.index(min(interval_distances))

        # Return the interval with the smallest distance
        tree_segment = tree_list[min_index]
        return tree_segment

    return best_segment
