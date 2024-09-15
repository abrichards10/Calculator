# This class will hold all of my equations/ formulas
# Use the math library for more complicated equations 

import math 

class Calculator: 

    def __init__(self) -> None:
        pass # Whenever this class is called, this will run 

    def add(self, a, b): # figure out the functionality of this function 
        return int(a) + int(b)

    def subtract(self, a, b): 
        return int(a) - int(b)
    
    def multiply(self, a, b):
        return int(a) * int(b)

    def divide(self, a, b):
        if ((int(a) != 0) and (int(b) != 0)):
            return int(a)/int(b)
        else: 
            print("Cannot divide by 0 or divide 0")

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def square_root(self, number):
        return math.sqrt(number)

    def logarithm(self, number, base=math.e):
        return math.log(number, base)

    def sine(self, angle_degrees):
        return math.sin(math.radians(angle_degrees))

    def cosine(self, angle_degrees):
        return math.cos(math.radians(angle_degrees))

    def tangent(self, angle_degrees):
        return math.tan(math.radians(angle_degrees))

    def factorial(self, n):
        if n < 0:
            return "Error: Factorial is not defined for negative numbers"
        return math.factorial(n)

    def permutation(self, n, r):
        return math.perm(n, r)

    def combination(self, n, r):
        return math.comb(n, r)

    def quadratic_formula(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real roots"
        elif discriminant == 0:
            x = -b / (2*a)
            return f"One root: {x}"
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Two roots: {x1} and {x2}"

    def absolute_value(self, number):
        return abs(number)

    def circle_area(self, radius):
        if radius < 0:
            return "Error: Radius cannot be negative"
        return math.pi * radius ** 2

