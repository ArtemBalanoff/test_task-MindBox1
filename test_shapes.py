# type:ignore
from shapes import Circle, Triangle, Square, Rectangle
from math import pi
import pytest

from constants import TEST_PRECISION


@pytest.mark.parametrize('constructor, args', [
    (Circle, (-1,)),
    (Square, (-1,)),
    (Rectangle, (-1, 4)),
    (Triangle, (-1, 2, 3)),
])
def test_negative_values(constructor, args):
    with pytest.raises(ValueError):
        constructor(*args)


@pytest.mark.parametrize('radius, correct_area', [
    (1, pi),
    (2, pi * 4),
    (0, 0),
    (0.5, pi * 0.25),
    (10, pi * 100),
])
def test_circle_area(radius, correct_area):
    assert Circle(
        radius, precision=TEST_PRECISION).area == round(correct_area, TEST_PRECISION)


@pytest.mark.parametrize('side, correct_area', [
    (1, 1),
    (2, 4),
    (0, 0),
    (0.5, 0.25),
    (10, 100),
])
def test_square_area(side, correct_area):
    assert Square(side, precision=TEST_PRECISION).area == round(
        correct_area, TEST_PRECISION)


@pytest.mark.parametrize('side_1, side_2, correct_area', [
    (1, 2, 2),
    (3, 4, 12),
    (0, 5, 0),
    (0.5, 0.5, 0.25),
    (10, 20, 200),
])
def test_rectangle_area(side_1, side_2, correct_area):
    assert Rectangle(side_1, side_2, precision=TEST_PRECISION).area == round(
        correct_area, TEST_PRECISION)


@pytest.mark.parametrize('a, b, c, correct_area', [
    (3, 4, 5, 6),
    (5, 5, 6, 12),
    (7, 8, 9, 26.8328),
    (10, 10, 10, 43.3013),
])
def test_triangle_area(a, b, c, correct_area):
    assert Triangle(a, b, c, precision=TEST_PRECISION).area == round(
        correct_area, TEST_PRECISION)


def test_right_triangle():
    assert Triangle(3, 4, 5).is_triangle_right == True
    assert Triangle(5, 6, 7).is_triangle_right == False


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 5, 20)
