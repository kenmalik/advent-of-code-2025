import pytest
from day_01.solution import rotate, rotate_with_passes


def test_rotate():
    assert rotate(5, 3) == 8
    assert rotate(5, 3, rotate_left=True) == 2

    assert rotate(5, 95) == 0
    assert rotate(5, 5, rotate_left=True) == 0

    assert rotate(5, 96) == 1
    assert rotate(5, 6, rotate_left=True) == 99

    assert rotate(5, 200) == 5
    assert rotate(5, 200, rotate_left=True) == 5


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
