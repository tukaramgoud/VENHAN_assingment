"""21. Inheritance and Polymorphism
Create a class hierarchy for `Shape`, `Circle`, and `Rectangle`. The base class Shape
should have methods to calculate area and perimeter, which are overridden in the derived
classes `Circle` and `Rectangle`.
"""
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


circle_1 = Circle(5)
print("Circle Area:", circle_1.area())
print("Circle Perimeter:", circle_1.perimeter())

rectangle_1 = Rectangle(4, 6)
print("Rectangle Area:", rectangle_1.area())
print("Rectangle Perimeter:", rectangle_1.perimeter())