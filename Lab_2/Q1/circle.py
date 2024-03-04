from shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def calculate_area(self):
        return round((pi * self.radius * self.radius), 2)
