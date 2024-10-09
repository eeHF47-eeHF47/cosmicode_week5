# Task 2: Implement a class hierarchy to represent geometric shapes (e.g., Circle, Rectangle, Triangle) with methods to calculate area and perimeter.
import math
# Define a base class called shape to represent a generic shape with methods for calculating area and perimeter
class Shape:
    # placeholder method for calculating area(implemented in derived classes)
    def calculate_area(self):
        pass
    # placeholder method for calculating perimeter(implemented in derived classes)
    def calculate_perimeter(self):
        pass
# define a derived class called circle,which inherits from the base class.
class Circle(Shape):
    # initialize circle with radius
    def __init__(self, radius):
        self.radius =radius
    # calculate and return the area of a circle using the formula:pi*r^2
    def calculate_area(self):
        return math.pi*self.radius**2
    # calculate and return the perimeter of a circle using the formula:2pi*r
    def calculate_area(self):
        return 2* math.pi*self.radius
    
# define a derived class called rectangle, which inherits from the base class.
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    # calculate and return the area of a rectangle using the formula:length*width
    def calculate_area(self):
        return self.length*self.width
    # calculate and return the perimeter of a rectangle using the formula:2*(length+width)
    def calculate_perimeter(self):
        return 2 *(self.length+self.width)
    
# define a derived class called triangle which inherits from base class.
class Triangle:
    def __init__(self, base, height,side1,side2,side3):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3

    # calculate the area of the triangle using formula :0.5 *base*height
    def calculate_area(self):
        return 0.5 *self.base*self.height

    # calculate and return the perimeterof the trainagle by adding the length of its 3 sides
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    

r=7
circle=Circle(r)
circle_area= circle.calculate_area()
circle_perimeter=circle.calculate_perimeter()

# print
print("RADIUS OF THE CIRCLE:",r)
print("CIRCLE AREA:",circle_area)
print("CIRCLE PERIMETER:",circle_perimeter)

# Rectangle
l=5
w=7
rectangle=Rectangle(l,w)
rectangle_area=rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

print("\nRECTANGLE: LEGNTH =",l,"WIDTH =",w)
print("RECTANGLE AREA:",rectangle_area)
print("RECTABNGLE PERIMETER:",rectangle_perimeter)

# Triangle
base=6
height=5
s1=5
s2=2
s3=6

triangle = Triangle(base,height,s1,s2,s3)
triangle_area=triangle.calculate_area()
triangle_perimeter =triangle.calculate_perimeter()
print("\nTRIANGLE AREA:",triangle_area)
print("TRIANGLE PERIMETER:",triangle_perimeter)