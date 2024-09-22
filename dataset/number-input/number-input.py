import streamlit as st

number = st.number_input(
    "Insert a number", value=None, placeholder=0
)
st.write("The current number is ", number)