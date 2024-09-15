import calculator
import streamlit as st

def main():
    equation = calculator.Calculator()

    st.title("Calculator")
    st.write("This is a calculator with basic and complex operations")

    # Input fields for two numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Create three rows with four buttons each
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10, col11, col12 = st.columns(4)  # New row for additional functions

    # Basic operations
    if col1.button("Add"):
        result = equation.add(num1, num2)
        st.write(f"{num1} + {num2} = {result}")

    if col2.button("Subtract"):
        result = equation.subtract(num1, num2)
        st.write(f"{num1} - {num2} = {result}")

    if col3.button("Multiply"):
        result = equation.multiply(num1, num2)
        st.write(f"{num1} * {num2} = {result}")

    if col4.button("Divide"):
        if num2 != 0:
            result = equation.divide(num1, num2)
            st.write(f"{num1} / {num2} = {result}")
        else:
            st.error("Cannot divide by zero!")

    # Complex operations
    if col5.button("Power"):
        result = equation.power(num1, num2)
        st.write(f"{num1} ^ {num2} = {result}")

    if col6.button("Square Root"):
        result = equation.square_root(num1)
        st.write(f"√{num1} = {result}")

    if col7.button("Logarithm"):
        if num1 > 0:
            result = equation.logarithm(num1)
            st.write(f"log({num1}) = {result}")
        else:
            st.error("Cannot calculate logarithm of non-positive number!")

    if col8.button("Factorial"):
        if num1.is_integer() and num1 >= 0:
            result = equation.factorial(int(num1))
            st.write(f"{int(num1)}! = {result}")
        else:
            st.error("Factorial is only defined for non-negative integers!")

    # New button for absolute value
    if col9.button("Absolute Value"):
        result = equation.absolute_value(num1)
        st.write(f"|{num1}| = {result}")

    # New button for circle area
    if col10.button("Circle Area"):
        if num1 >= 0:
            result = equation.circle_area(num1)
            st.write(f"Area of circle with radius {num1} = {result}")
        else:
            st.error("Radius cannot be negative!")

if __name__ == "__main__":
    main()
