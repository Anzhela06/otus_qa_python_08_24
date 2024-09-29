from src.triangle import Triangle
import pytest


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter',
[
    (3, 4, 5, 12),
    (1.5, 2.5, 3.6, 7.6),
    (0, -1, 3, 10)
],
    ids=['integer', 'float', 'negative']
)

def test_triangle_perimeter(send_screenshot, side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == perimeter, f'Perimeter should be {perimeter}'


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
[
    (3, 4, 5, 12, 6),
    (1.5, 2.5, 3.6, 7.6, 1.5),
    (0, -1, 3, 10, 10),

],
    ids=['integer', 'float', 'negative']
)


def test_triangle_area(send_screenshot, side_a, side_b, side_c, perimeter, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area, f'Area should be {area}'

def test_triangle_equal_sides():
    side_a = 1
    side_b = 1
    side_c = 1
    perimeter = 3
    t = Triangle(side_a, side_b, side_c)
    perimeter = t.get_perimeter
    assert perimeter == perimeter, f'Perimeter should be {perimeter}'