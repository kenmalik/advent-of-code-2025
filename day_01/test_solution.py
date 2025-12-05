from day_01.solution import rotate


def test_rotate():
    assert rotate(5, 3) == 8
    assert rotate(5, 3, rotate_left=True) == 2

    assert rotate(5, 95) == 0
    assert rotate(5, 5, rotate_left=True) == 0

    assert rotate(5, 96) == 1
    assert rotate(5, 6, rotate_left=True) == 99

    assert rotate(5, 200) == 5
    assert rotate(5, 200, rotate_left=True) == 5
