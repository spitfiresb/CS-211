"""
UO CIS 211 Code Demo, Week 4
Created by: Haoran Wang
______________________________________________________________________
Overview:
Create a Python class named 'Triangle'. 
Then, create two sub-classes "EquilateralTriangle" and "IsoscelesTriangle" to inherit from Triangle.

Details:
Triangle class has three attributes:
a, b, c to represent three sides of a triangle
they are of integer type
Triangle class has a function area() to calculate the area:
returns a float
Formula: 
s = (a + b + c) / 2 
area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
Equilateral triangle:
a to represent one side of a triangle
In an equilateral triangle: a = b = c
use super() to call its parent's constructor
Override the area() function:
returns a float
Formula: math.sqrt(3) * a * a / 4
Isosceles triangle:
a, c
In an Isosceles triangle: a = b
use super() to call its parent's constructor
Override the area() function:
returns a float
Formula: 0.5 * math.sqrt(a * a - 0.25 * c * c) * c

Test for correctness:
Create a main function
Create three Triangle objects: t1 (triangle), t2 (equilateral), t3(isosceles) t1: 4, 13, 15 t2: 10, 10, 10 t3: 6, 6, 8
Print out the area of t1, t2, and t3
area of t1 = 24.00 
area of t1 = 43.30 
area of t1 = 17.89

"""
import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s= ((self.a + self.b + self.c) / 2)
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) 
        return area
    
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        """self.a = a
        self.b = self.a
        self.c = self.a"""

    
        super().__init__(a, a, a)


        

class IsoscelesTriangle(Triangle):
    def __init__(self, a, c):
        """self.a = a
        self.b = self.a
        self.c = c"""

        super().__init__(a, a, c)



if __name__ == "__main__":
    t1 = Triangle(4, 13, 15)
    print("area of t1= ", "{:.2f}".format(t1.area()))
    assert round(t1.area(), 2) == 24.00

    t2 = EquilateralTriangle(10)
    print("area of t2= ", "{:.2f}".format(t2.area()))
    assert round(t2.area(), 2) == 43.30

    t3 = IsoscelesTriangle(6, 8)
    print("area of t3= ", "{:.2f}".format(t3.area()))
    assert round(t3.area(), 2) == 17.89

