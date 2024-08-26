import calculator
import streamlit as st

def main():
    equation = calculator.Calculator()

    st.title("Calculator")
    st.write("This is a calculator with basic and complex operations")

    # Input fields for two numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Create two rows with four buttons each
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

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

if __name__ == "__main__":
    main()

