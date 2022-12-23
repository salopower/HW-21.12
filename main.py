from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width

    def draw(self):
        for i in range(1, self.width + 1):
            print(" " * (self.width - i) + "*" * i)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.height):
            print("*" * self.width)


shapes = [Triangle(5), Rectangle(6, 4)]

for shape in shapes:
    shape.draw()
