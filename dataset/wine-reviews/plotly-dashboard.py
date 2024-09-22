import streamlit as st
import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

import plotly.graph_objs as go

scatter = go.Scatter(x=reviews.head(1000)['points'], y=reviews.head(1000)['price'], mode='markers')
fig = go.Figure(data = [scatter])
st.plotly_chart(fig)

histo = go.Histogram2dContour(x=reviews.head(500)['points'], 
                             y=reviews.head(500)['price'], 
                             contours=go.Contours(coloring='heatmap'))
scatter2 = go.Scatter(x=reviews.head(1000)['points'], y=reviews.head(1000)['price'], mode='markers')
fig = go.Figure(data = [histo, scatter2])
st.plotly_chart(fig)

df = reviews.assign(n=0).groupby(['points', 'price'])['n'].count().reset_index()
df = df[df["price"] < 100]
v = df.pivot(index='price', columns='points', values='n').fillna(0).values.tolist()

surface = go.Surface(z=v)
fig = go.Figure(data = [surface])
st.plotly_chart(fig)

df = reviews['country'].replace("US", "United States").value_counts()

choropleth = go.Choropleth(
    locationmode='country names',
    locations=df.index.values,
    text=df.index,
    z=df.values
)
fig = go.Figure(data = [choropleth])
st.plotly_chart(fig)
