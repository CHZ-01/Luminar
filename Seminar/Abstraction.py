# Defining class
class Rectangle:
    # Defining methods
    def __init__(self, length, width):
        self.length = length  # Private attribute
        self.width = width    # Private attribute

    def area(self):
        A = self.length * self.width
        print("Area:",A)

    def perimeter(self):
        P = 2*(self.length + self.width)
        print("Perimeter:",P)

# Calling objects
rect = Rectangle(5, 3)
# Calling methods, the actual code will not be revealed
rect.area()
rect.perimeter()