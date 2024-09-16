import math
from abc import ABC, abstractmethod


class Figure(ABC):


    @property
    @abstractmethod
    def get_area(self):
        pass


    @property
    @abstractmethod
    def get_perimeter(self):
        pass


    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"Argument {figure} must belong to class Figure")
        return self.get_area + figure.get_area

class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <=0 :
            raise ValueError("Rectangle sides can't be less or equals to 0")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = self.side_a + self.side_b + self.side_c
        self.area = math.sqrt(self.perimeter / 2 * (self.perimeter / 2 - self.side_a) * (self.perimeter / 2 - self.side_b) * (self.perimeter / 2  - self.side_c))

    @property
    def get_area(self):
         return math.sqrt(self.perimeter / 2 * (self.perimeter / 2 - self.side_a) * (self.perimeter / 2 - self.side_b) * (self.perimeter / 2  - self.side_c))

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c




t = Triangle (3, 3, 1)

