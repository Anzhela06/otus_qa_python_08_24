import math
from src.figure import Figure

class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <=0 :
            raise ValueError("Rectangle sides can't be less or equals to 0")
        if side_a == side_b and side_b == side_c :
            raise ValueError ("Равносторонний треугольник")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = self.side_a + self.side_b + self.side_c



    @property
    def get_area(self):
         return math.sqrt(self.perimeter / 2 * (self.perimeter / 2 - self.side_a) * (self.perimeter / 2 - self.side_b) * (self.perimeter / 2  - self.side_c))

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c








