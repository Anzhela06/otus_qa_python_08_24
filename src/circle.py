import math
from src.figure import Figure



class Circle(Figure):

    def __init__(self, side_r):
        if side_r <=0 :
            raise ValueError("Radius can't be less or equal to 0")

        self.side_r = side_r


    @property
    def get_area(self):
         return math.pi * self.side_r ** 2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.side_r

