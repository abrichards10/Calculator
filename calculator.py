# This class will hold all of my equations/ formulas
# Use the math library for more complicated equations 

import math 

class Calculator: 

    def __init__(self) -> None:
        pass # Whenever this class is called, this will run 

    def add(self, a, b): # figure out the functionality of this function 
        return a + b

    def subtract(self, a, b): 
        return a - b
    
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if ((a != 0) and (b != 0)):
            return a/b
        else: 
            print("Cannot divide by 0 or divide 0")