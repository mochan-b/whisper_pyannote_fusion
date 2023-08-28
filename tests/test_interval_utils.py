from intervaltree import IntervalTree
from whisper_pyannote_fusion.interval_utils import get_largest_intersection_segment, get_closest_intersection_segment


def test_largest_intersection_interval():
    """
    Test the largest intersection interval function
    """
    tree = IntervalTree()
    tree.addi(0, 10, '0')
    tree.addi(12, 20, '1')
    tree.addi(24, 27, '0')
    tree.addi(30, 40, '2')
    segment = {'start': 2, 'end': 13}
    largest_intersection_segment = get_largest_intersection_segment(tree, segment)
    assert largest_intersection_segment.data == '0'
    assert largest_intersection_segment.begin == 0
    assert largest_intersection_segment.end == 10
    assert largest_intersection_segment.length() == 10
    segment = {'start': 13, 'end': 14}
    largest_intersection_segment = get_largest_intersection_segment(tree, segment)
    assert largest_intersection_segment.data == '1'
    assert largest_intersection_segment.begin == 12
    assert largest_intersection_segment.end == 20
    assert largest_intersection_segment.length() == 8
    segment = {'start': 14, 'end': 20}
    largest_intersection_segment = get_largest_intersection_segment(tree, segment)
    assert largest_intersection_segment.data == '1'
    assert largest_intersection_segment.begin == 12
    assert largest_intersection_segment.end == 20
    assert largest_intersection_segment.length() == 8
    segment = {'start': 22, 'end': 38}
    largest_intersection_segment = get_largest_intersection_segment(tree, segment)
    assert largest_intersection_segment.data == '2'
    assert largest_intersection_segment.begin == 30
    assert largest_intersection_segment.end == 40
    assert largest_intersection_segment.length() == 10
    segment = {'start': 38, 'end': 40}
    largest_intersection_segment = get_largest_intersection_segment(tree, segment)
    assert largest_intersection_segment.data == '2'
    assert largest_intersection_segment.begin == 30
    assert largest_intersection_segment.end == 40
    assert largest_intersection_segment.length() == 10
    segment = {'start': 42, 'end': 50}
    largest_intersection_segment = get_largest_intersection_segment(tree, segment)
    assert largest_intersection_segment is None


def test_get_closest_intersection_segment():
    """
    Test the closest intersection interval function
    """
    tree = IntervalTree()
    tree.addi(0, 10, '0')
    tree.addi(12, 20, '1')
    tree.addi(24, 27, '0')
    tree.addi(30, 40, '2')
    segment = {'start': 2, 'end': 13}
    closest_intersection_segment = get_closest_intersection_segment(tree, segment)
    assert closest_intersection_segment.data == '0'
    assert closest_intersection_segment.begin == 0
    assert closest_intersection_segment.end == 10
    assert closest_intersection_segment.length() == 10

    segment = {'start': 10.1, 'end': 10.5}
    closest_intersection_segment = get_closest_intersection_segment(tree, segment)
    assert closest_intersection_segment.data == '0'

    segment = {'start': 11.5, 'end': 11.75}
    closest_intersection_segment = get_closest_intersection_segment(tree, segment)
    assert closest_intersection_segment.data == '1'
    assert closest_intersection_segment.begin == 12
    assert closest_intersection_segment.end == 20
    assert closest_intersection_segment.length() == 8


def test_find_all_intersecting_intervals():
    """
    Test of the overlap and envelop functions of the interval tree
    """
    main_interval = {'start': 1., 'end': 3.}
    interval_1 = {'start': 0.9, 'end': 1.1}
    interval_2 = {'start': 1.1, 'end': 1.2}
    interval_3 = {'start': 2.9, 'end': 3.1}
    interval_4 = {'start': 3.1, 'end': 3.2}
    intervals = [interval_1, interval_2, interval_3, interval_4]

    # All the intervals to the interval tree
    tree = IntervalTree()
    for interval in intervals:
        tree.addi(interval['start'], interval['end'], interval)

    # Find all the intersecting intervals to main_interval
    intersecting_intervals = tree.envelop(main_interval['start'], main_interval['end'])
    assert len(intersecting_intervals) == 1

    intersecting_intervals = tree.overlap(main_interval['start'], main_interval['end'])
    assert len(intersecting_intervals) == 3