import streamlit as st

st.button('Click me')

st.radio("Pick your sex", ["Male", "Female", "other"])

st.selectbox("Pick your course", ["Machine Learning", "Computer Science","Psychology"])

st.multiselect("Choose department(s)", ["Content", "Sales", "Marketing"])

st.select_slider("Rating", ["Bad", "Good", "Outstanding"])

st.slider("Enter #", 0, 100)
