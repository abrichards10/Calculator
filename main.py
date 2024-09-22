import calculator
import streamlit as st

def main():
    equation = calculator.Calculator()

    st.title("Calculator")

    # Input field for display
    display = st.text_input("", value="0", key="display")

    # Create a container for buttons
    with st.container():
        # Create button layout with smaller columns
        cols = st.columns(7)
        
        # Number buttons
        # First row: 0, 1, 2
        if cols[1].button("0", key="btn_0"):
            display += "0"
        if cols[2].button("1", key="btn_1"):
            display += "1"
        if cols[3].button("2", key="btn_2"):
            display += "2"

        # Second row: 3, 4, 5
        if cols[1].button("3", key="btn_3"):
            display += "3"
        if cols[2].button("4", key="btn_4"):
            display += "4"
        if cols[3].button("5", key="btn_5"):
            display += "5"

        # Third row: 6, 7, 8
        if cols[1].button("6", key="btn_6"):
            display += "6"
        if cols[2].button("7", key="btn_7"):
            display += "7"
        if cols[3].button("8", key="btn_8"):
            display += "8"

        # Fourth row: 9
        if cols[1].button("9", key="btn_9"):
            display += "9"
        # Operator buttons
        operators = ['+', '-', '*', '/']
        for i, op in enumerate(operators):
            if cols[3].button(op, key=f"btn_{op}"):
                display += op

        # Function buttons
        functions = ['sqrt', 'log', 'abs', 'fact']
        for i, func in enumerate(functions):
            if cols[4 + i // 2].button(func, key=f"btn_{func}"):
                display = f"{func}({display})"

        # Special buttons
        if cols[6].button("C", key="btn_clear"):
            display = "0"
        if cols[6].button("=", key="btn_equals"):
            try:
                result = eval(display)
                display = str(result)
            except:
                display = "Error"

    # Show result
    st.text_input("Result", value=display, key="result", disabled=True)

if __name__ == "__main__":
    main()
