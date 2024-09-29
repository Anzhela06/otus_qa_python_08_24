from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "side_r, area",
    [ (1, 3.14),
      (2.5, 19.63),
      (-2, 4)
    ],
    ids =['integer', 'float', 'negative']
)

def test_circle_area(side_r, area):
    c  = Circle(side_r)
    assert round(c.get_area, 2) == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_r, perimeter",
    [ (1, 6.28),
      (2.5, 15.71),
      (0, 0)
    ],
    ids =['integer', 'float', 'negative']
)

def test_circle_perimeter(side_r, perimeter):
    c  = Circle(side_r)
    assert round(c.get_perimeter, 2) == perimeter, f'Perimeter should be {area}'

