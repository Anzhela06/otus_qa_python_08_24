from src.rectangle import Rectangle
import pytest



@pytest.mark.parametrize(
    "side_a, side_b, area",
    [ (2, 3, 6),
      (2.5, 3.5, 8.75),
      (0, 1, 1)
    ],
    ids =['integer', 'float', 'negative']
)

def test_rectangle_area(create_api,side_a, side_b, area):
    r = Rectangle (side_a, side_b)
    assert r.get_area == area, f'Area should be {area}'



@pytest.mark.parametrize(
    "side_a, side_b, perimeter",
    [ (2, 3, 10),
      (2.5, 3.5, 12),
      (0, 1, 1)
    ],
    ids =['integer', 'float', 'negative']
)


def test_rectangle_perimeter(create_api, side_a, side_b, perimeter):
    r = Rectangle (side_a, side_b)
    assert r.get_perimeter == perimeter, f'Area should be {perimeter}'