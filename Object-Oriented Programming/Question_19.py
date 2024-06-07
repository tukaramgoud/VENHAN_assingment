'''19. Create a class `Rectangle` with the following attributes and methods:
*Attributes: length, width
*Methods:
*`__init__(self, length: float, width: float)`: Constructor to initialize the attributes.
*`area(self) -> float`: Method to calculate the area of the rectangle.
*`perimeter(self) -> float`: Method to calculate the perimeter of the rectangle.'''


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    
    def area(self):
        return self.width * self.length 
    
    def perimeter(self):
        return 2 * (self.width + self.length)

rectangel = Rectangle(4.4,6.5)
print(rectangel.area())
print(rectangel.perimeter())