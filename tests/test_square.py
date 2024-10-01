from src.square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, area",
    [ (100, 10000),
      (2.5, 8.75)
    ],
    ids =['integer', 'float']
)

def test_square_area_positive(create_api,side_a, area):
    s = Square(side_a)
    assert s.get_area == area, f'Area should be {area}'

@pytest.mark.parametrize(
    "side_a, area",
    [ (0, 0),
      (-2, 4)
    ],
    ids =['0 values', 'negative']
)

def test_square_area_negative(create_api,side_a, area):
    with pytest.raises(ValueError, match=None):
        s = Square(side_a)
        assert s.get_area == area, f'Area should be {area}'




@pytest.mark.parametrize(
    "side_a, perimeter",
    [ (100, 400),
      (2.5, 10)
    ],
    ids =['integer', 'float']
)

def test_square_perimeter_positive(create_api, side_a, perimeter):
    s = Square(side_a)
    assert s.get_perimeter == perimeter, f'Perimeter should be {perimeter}'


@pytest.mark.parametrize(
    "side_a, perimeter",
    [ (0, 400),
      (-2.5, 10)
    ],
    ids =['0 values', 'negative']
)

def test_square_perimeter_negative(create_api, side_a, perimeter):
    with pytest.raises(ValueError):
       s = Square(side_a)
       assert s.get_perimeter == perimeter, f'Perimeter should be {perimeter}'