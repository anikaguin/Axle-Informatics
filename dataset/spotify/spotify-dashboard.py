import streamlit as st
#see which imports are not used and remove 
import pandas as pd #used
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt

#df=pd.read_csv('/kaggle/input/top-hits-spotify-from-20002019/songs_normalize.csv')
#use^ when uploading or just provide it with notebook? I think provide
#do it depending on the notebooks hub, just github we needed data/name.cvs yk?
dataset = "spotify\songs_normalize.csv"
df = pd.read_csv(dataset)

df.duplicated().value_counts()

#dropping duplicates
df.drop_duplicates(inplace=True)

#dropping columns without int/float types 
#heatmap

fig=px.imshow(df.drop(columns = ['artist', 'song', 'explicit', 'genre'], inplace=False).corr(),text_auto=True,height=800,width=800,color_continuous_scale=px.colors.sequential.Greens,aspect='auto',title='<b>paiwise correlation of columns')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

#histograms
fig=make_subplots(rows=3,cols=3,subplot_titles=('<i>popularity', '<i>danceability', '<i>energy', '<i>loudness', '<i>speechiness', '<i>acousticness', '<i>liveness', '<i>valence', '<i>tempo'))
fig.add_trace(go.Histogram(x=df['popularity'],name='popularity'),row=1,col=1)
fig.add_trace(go.Histogram(x=df['danceability'],name='danceability'),row=1,col=2)
fig.add_trace(go.Histogram(x=df['energy'],name='energy'),row=1,col=3)
fig.add_trace(go.Histogram(x=df['loudness'],name='loudness'),row=2,col=1)
fig.add_trace(go.Histogram(x=df['speechiness'],name='speechiness'),row=2,col=2)
fig.add_trace(go.Histogram(x=df['acousticness'],name='acousticness'),row=2,col=3)
fig.add_trace(go.Histogram(x=df['liveness'],name='liveness'),row=3,col=1)
fig.add_trace(go.Histogram(x=df['valence'],name='valence'),row=3,col=2)
fig.add_trace(go.Histogram(x=df['tempo'],name='tempo'),row=3,col=3)
fig.update_layout(height=900,width=900,title_text='<b>Feature Distribution')
fig.update_layout(template='plotly_dark',title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

fig=px.area(df.groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',markers=True,labels={'song':'Total songs'},color_discrete_sequence=['green'],title='<b>Year by Year Songs collection')
fig.update_layout(hovermode='x',title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

fig=px.histogram(df.groupby('genre',as_index=False).count().sort_values(by='song',ascending=False),x='genre',y='song',color_discrete_sequence=['green'],template='plotly_dark',marginal='box',title='<b>Total songs based on genres</b>')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

fig=px.histogram(df.groupby('genre',as_index=False).sum().sort_values(by='popularity',ascending=False),x='genre',y='popularity',color_discrete_sequence=['lightgreen'],template='plotly_dark',marginal='box',title='<b>Popular genres based on pouplarity</b>')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

px.bar(df.groupby('artist',as_index=False).count().sort_values(by='song',ascending=False).head(50),x='artist',y='song',labels={'song':'Total Songs'},width=1000,color_discrete_sequence=['green'],text='song',title='<b> List of Songs Recorded by Each Singer')
st.plotly_chart(fig, use_container_width=True)

px.bar(df.groupby('artist',as_index=False).sum().sort_values(by='popularity',ascending=False).head(30),x='artist',y='popularity',color_discrete_sequence=['lightgreen'],template='plotly_dark',text='popularity',title='<b>Top 30 Popular Singers')
st.plotly_chart(fig, use_container_width=True)

fig=px.line(df.sort_values(by='popularity',ascending=False).head(25),x='song',y='popularity',hover_data=['artist'],color_discrete_sequence=['green'],markers=True,title='<b> Top 25 songs in Spotify')
st.plotly_chart(fig, use_container_width=True)

fig=px.treemap(df,path=[px.Constant('Singer'),'artist','genre','song'],values='popularity',title='<b>TreeMap of Singers Playlist')
fig.update_traces(root_color='lightgreen')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

fig=px.pie(df.groupby('explicit',as_index=False).count().sort_values(by='song',ascending=False),names='explicit',values='song',labels={'song':'Total songs'},hole=.6,color_discrete_sequence=['green','crimson'],template='plotly_dark',title='<b>Songs having explicit content')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig, use_container_width=True)

fig=px.area(df[df['explicit']==True].groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',labels={'song':'Total songs'},markers=True,color_discrete_sequence=['red'],template='plotly_dark',title='<b>Yearwise explicit content songs')
fig.update_layout(hovermode='x')
st.plotly_chart(fig, use_container_width=True)

fig =px.box(df,x='explicit',y='popularity',color='explicit',template='plotly_dark',color_discrete_sequence=['cyan','magenta'],title='<b>popularity based on explicit content')
st.plotly_chart(fig, use_container_width=True)

fig=px.scatter(df,x='tempo',y='popularity',color='tempo',color_continuous_scale=px.colors.sequential.Plasma,template='plotly_dark',title='<b>Tempo Versus Popularity')
st.plotly_chart(fig, use_container_width=True)

fig=px.scatter(df,x='speechiness',y='popularity',color='speechiness',color_continuous_scale=px.colors.sequential.Plasma,template='plotly_dark',title='<b> Speechiness Versus Popularity')
st.plotly_chart(fig, use_container_width=True)

fig=px.scatter(df,x='energy',y='danceability',color='danceability',color_continuous_scale=px.colors.sequential.Plotly3,template='plotly_dark',title='<b>Energy Versus Danceability')
st.plotly_chart(fig, use_container_width=True)

px.scatter(df,x='energy',y='loudness',color_discrete_sequence=['lightgreen'],template='plotly_dark',title='<b>Energy versus Loudness correlation')
st.plotly_chart(fig, use_container_width=True)

#pop is most popular genre 


#top 3 singers who recorded maximum songs, Rihanna Drake Eminem
#top 3 popular singers Rihanna Enminem Drake 
#top 3 popular songs, sweater weather by the Neighborhood, Another Love by Tom odell, Without me by eminem
st.title("Top Three Singers Who Recorded Maximum Songs")
st.write('Top 3 Singers')
fig = px.bar()