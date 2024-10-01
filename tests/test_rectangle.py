from src.rectangle import Rectangle
import pytest



@pytest.mark.parametrize(
    "side_a, side_b, area",
    [ (2, 3, 6),
      (2.5, 3.5, 8.75)
    ],
    ids =['integer', 'float']
)

def test_rectangle_area_positive(create_api,side_a, side_b, area):
    r = Rectangle (side_a, side_b)
    assert r.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [ (1, 0, 6),
      (-1, 3, 1)
    ],
    ids =['0 values', 'negative']
)

def test_rectangle_area_negative(create_api,side_a, side_b, area):
    with pytest.raises(ValueError,match =None):
        r = Rectangle (side_a, side_b)
        assert r.get_area == area, f'Area should be {area}'



@pytest.mark.parametrize(
    "side_a, side_b, perimeter",
    [ (2, 3, 10),
      (2.5, 3.5, 12)
    ],
    ids =['integer', 'float']
)


def test_rectangle_perimeter(create_api, side_a, side_b, perimeter):
    r = Rectangle (side_a, side_b)
    assert r.get_perimeter == perimeter, f'Area should be {perimeter}'

@pytest.mark.parametrize(
    "side_a, side_b, perimeter",
    [ (0, 0, 6),
      (-1, 3, 1)
    ],
    ids =['0 values', 'negative']
)


def test_rectangle_perimeter_negative(create_api, side_a, side_b, perimeter):
    with pytest.raises(ValueError,match =None):
        r = Rectangle (side_a, side_b)
        assert r.get_perimeter == perimeter, f'Perimeter should be {perimeter}'