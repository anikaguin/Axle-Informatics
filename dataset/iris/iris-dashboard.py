import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns 
import matplotlib.pyplot as plt

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

fig = px.scatter(iris, x = "SepalLengthCm", y="SepalWidthCm")
st.plotly_chart(fig)

fig = sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=10)
st.pyplot(fig)

g = sns.FacetGrid(iris, hue="Species", height=7) 
g.map(plt.scatter, "SepalLengthCm", "SepalWidthCm") 
g.add_legend()
st.pyplot(g.figure)

fig = px.box(iris, x="Species", y="PetalLengthCm")
st.plotly_chart(fig)

