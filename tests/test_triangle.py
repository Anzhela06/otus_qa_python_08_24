from src.triangle import Triangle
import pytest


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter',
[
    (3, 4, 5, 12),
    (1.5, 2.5, 3.6, 7.6)
],
    ids=['integer', 'float']
)

def test_triangle_perimeter_positive(send_screenshot, side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == perimeter, f'Perimeter should be {perimeter}'



@pytest.mark.parametrize('side_a, side_b, side_c, perimeter',
[
    (0, 0, 5, 12),
    (-1.5, 2.5, 3.6, 7.6)
],
    ids=['0 values', 'negative']
)

def test_triangle_perimeter_negative(send_screenshot, side_a, side_b, side_c, perimeter):
    with pytest.raises(ValueError):
       t = Triangle(side_a, side_b, side_c)
       assert t.get_perimeter == perimeter, f'Perimeter should be {perimeter}'




@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
[
    (3, 4, 5, 12, 6),
    (1.5, 2.5, 3.6, 7.6, 1.51)
],
    ids=['integer', 'float']
)


def test_triangle_area_positive(send_screenshot, side_a, side_b, side_c, perimeter, area):
    t = Triangle(side_a, side_b, side_c)
    assert round(t.get_area,2) == area, f'Area should be {area}'



@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
[
    (0, 4, 5, 12, 6),
    (-1.5, 2.5, 3.6, 7.6, 1.51)
],
    ids=['0 values', 'negative']
)


def test_triangle_area_negative(send_screenshot, side_a, side_b, side_c, perimeter, area):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert round(t.get_area,2) == area, f'Area should be {area}'



@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
[
    (7, 7, 7, 12, 6)
],
    ids=['equal_sides']
)


def test_triangle_equal_sides(send_screenshot, side_a, side_b, side_c, perimeter, area):
    with pytest.raises(ValueError, match='Равносторонний треугольник'):
        t = Triangle(side_a, side_b, side_c)
        assert round(t.get_area,2) == area, f'Area should be {area}'