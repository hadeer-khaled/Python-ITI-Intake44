from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name, color):
        self.name = name
        self._color = color

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    @abstractmethod
    def calculate_area(self):
        pass
