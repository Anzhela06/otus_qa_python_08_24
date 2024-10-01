from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "side_r, area",
    [ (1, 3.14),
      (2.5, 19.63)
    ],
    ids =['integer', 'float']
)

def test_circle_area_positive(side_r, area):
    c  = Circle(side_r)
    assert round(c.get_area, 2) == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_r, area",
    [ (0, 6.28),
      (-666, 0)
    ],
    ids =['0 values', 'negative']
)

def test_circle_area_negative(side_r, area):
    with pytest.raises(ValueError):
       c  = Circle(side_r)
       assert round(c.get_area, 2) == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_r, perimeter",
    [ (1, 6.28),
      (2.5, 15.71)
      ],
    ids =['integer', 'float']
)

def test_circle_perimeter_positive(side_r, perimeter):
        c  = Circle(side_r)
        assert round(c.get_perimeter, 2) == perimeter, f'Perimeter should be {perimeter}'




@pytest.mark.parametrize(
    "side_r, perimeter",
    [ (0, 3.14),
      (-2.5, 19.63)
      ],
    ids=['0 values', 'negative']
)



def test_circle_perimeter_negative(side_r, perimeter):
    with pytest.raises(ValueError):
        c  = Circle(side_r)
        assert round(c.get_perimeter, 2) == perimeter, f'Perimeter should be {perimeter}'