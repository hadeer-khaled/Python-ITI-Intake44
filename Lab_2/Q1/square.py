from shape import Shape

class Square(Shape):
    def __init__(self, name, color, side_length):
        super().__init__(name, color)
        self.side_length = side_length

    def calculate_area(self):
        return round((self.side_length * self.side_length), 2)
