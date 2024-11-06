import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Dropdown to select operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on the operation selected
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero")

# Display the result
if result is not None:
    st.write(f"The result is: {result}")
