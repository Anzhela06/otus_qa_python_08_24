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



class Circle(Figure):

    def __init__(self, side_r):
        if side_r <=0 :
            raise ValueError("Radius can't be less or equals to 0")

        self.side_r = side_r
        self.perimeter = 2 * math.pi * self.side_r
        self.area = math.pi * self.side_r ** 2

    @property
    def get_area(self):
         return math.pi * self.side_r ** 2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.side_r




c = Circle (0)
print(c.get_perimeter)
print(c.get_area)