import pandas as pd
import numpy as np
import streamlit as st 

st.title("Bar Chart")


data = pd.DataFrame(np.random.randn(50, 2), columns=["x","y"])
st.bar_chart(data)
st.title("Line chart")
st.line_chart(data)

st.title("Area Chart")
st.area_chart(data)