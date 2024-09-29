from src.square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, area",
    [ (100, 10000),
      (2.5, 8.75),
      (-2, 4)
    ],
    ids =['integer', 'float', 'negative']
)

def test_square_area(create_api,side_a, area):
    s = Square(side_a)
    assert s.get_area == area, f'Area should be {area}'



@pytest.mark.parametrize(
    "side_a, perimeter",
    [ (100, 400),
      (2.5, 10),
      (-3.5, 0)
    ],
    ids =['integer', 'float', 'negative']
)

def test_square_perimeter(create_api, side_a, perimeter):
    s = Square(side_a)
    assert s.get_perimeter == perimeter, f'Perimeter should be {perimeter}'