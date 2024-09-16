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

class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <=0 :
            raise ValueError("Rectangle sides can't be less than 0")


        self.side_a = side_a
        self.side_b = side_b
        self.area = self.side_a * self.side_b
        self.perimeter = (self.side_a + self.side_b) * 2

    @property
    def get_area(self):
         return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less or equals to 0")
        super().__init__(side_a, side_a)

s = Square (8)
print(s.area)


