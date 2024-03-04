from square import Square
from circle import Circle
from rectangle import Rectangle

square= Square("square1","black" , 5)
rectangle= Rectangle("rectangle1","black" , 5 , 5)
circle= Circle("circle1","black" , 5)

print(f"Area of Square with side length = 5 is : {square.calculate_area()} \n")
print(f"Area of Rectangle with length and width = 5 is : {rectangle.calculate_area()}\n")
print(f"Area of Circle with raduis = 5 is : {circle.calculate_area()}\n")