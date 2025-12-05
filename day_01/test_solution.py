import pytest
from day_01.solution import rotate, rotate_with_passes


@pytest.mark.parametrize(
    "start,amount,rotate_left,expected",
    [
        (5, 3, False, 8),
        (5, 3, True, 2),
        (5, 95, False, 0),
        (5, 5, True, 0),
        (5, 96, False, 1),
        (5, 6, True, 99),
        (5, 200, False, 5),
        (5, 200, True, 5),
    ],
)
def test_rotate(start, amount, rotate_left, expected):
    assert rotate(start, amount, rotate_left) == expected


@pytest.mark.parametrize(
    "start,amount,rotate_left,next_expected,passes_expected",
    [
        (5, 5, True, 0, 1),
        (5, 95, False, 0, 1),
        (5, 1, True, 4, 0),
        (5, 1, False, 6, 0),
        (5, 10, True, 95, 1),
        (5, 100, False, 5, 1),
        (5, 200, True, 5, 2),
        (5, 200, False, 5, 2),
        (5, 205, True, 0, 3),
        (5, 295, False, 0, 3),
        (0, 1, True, 99, 0),
        (0, 1, False, 1, 0),
        (0, 100, True, 0, 1),
        (0, 100, False, 0, 1),
        (0, 101, True, 99, 1),
        (0, 101, False, 1, 1),
        (0, 200, True, 0, 2),
        (0, 200, False, 0, 2),
        (0, 201, True, 99, 2),
        (0, 201, False, 1, 2),
    ],
)
def test_rotate_with_passes(start, amount, rotate_left, next_expected, passes_expected):
    next, passes = rotate_with_passes(start, amount, rotate_left)
    assert next == next_expected
    assert passes == passes_expected
