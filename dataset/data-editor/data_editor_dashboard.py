import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 2), columns=["x","y"])

table = st.data_editor(df)
