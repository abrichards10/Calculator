# This is where I will: 
## Ask the user what they would like to do/ what equation 
## Call those functions in the calculator file 
## Put that in a while loop to see if they want to use another equation 

import calculator

def main(): 

    equation = calculator.Calculator()

    print("Hello! Welcome to the Calculator")
    while True: 
        user_input = input("Please choose what you would like to do:\n(1)Add\n(2)Subtract\n(3)Multiply\n(4)Divide")
        
        if (user_input == "1"): 
            add_input = input("Give me the first number you want to add")
            add_input1 = input("Give me the second number you want to add")
            print(f"{add_input} + {add_input1} = {equation.add(add_input, add_input1)}")

        if (user_input == "2"): 
            subtract_input = input("Give me the number you want to subtract from")
            subtract_input1 = input("Give me the number you want to subtract")
            print(f"{subtract_input} - {subtract_input1} = {equation.subtract(subtract_input, subtract_input1)}")

        if (user_input == "3"): 
            subtract_input = input("Give me the number you want to subtract from")
            subtract_input1 = input("Give me the number you want to subtract")
            print(f"{subtract_input} - {subtract_input1} = {equation.subtract(subtract_input, subtract_input1)}")
        if (user_input == "4"): 
            pass
        else: 
            print("Not a valid option ")
    


main()