#!/usr/bin/env python
# coding: utf-8

# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         SPOTIFY DATA VISUALIZATION
#     </h3>
#     </div>

# ![](https://c.tenor.com/iczjaEFdW20AAAAC/spotify-music.gif)

# <p>Spotify transformed music listening forever when it launched in Sweden in 2008. Discover, manage and share over 70m tracks for free, or upgrade to Spotify Premium to access exclusive features including offline mode, improved sound quality, and an ad-free music listening experience. 
# 
# Today, Spotify is the most popular global audio streaming service with 365m users, including 165m subscribers across 178 markets. They are the largest driver of revenue to the music business today.</p>

# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         TABLE OF CONTENTS
#     </h3>
#     </div>
#   
#   
# <br> 
# <br>
# <br>
# 
# <p>
#     <b>1. IMPOPRTING LIBRARIES AND LOADING DATA</b>
# </p>
# <p>
#     <b>2. DATA INFORMATION </b>
# </p>
# <p>
#     <b>3. EXPLORATORY DATA ANALYSIS </b>
# </p>
# <p>
#     <b>4. CONCLUSION </b>
# </p>
# <p>
#     <b>5. END </b>
# </p>

# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         IMPORTING LIBRARIES AND LOADING DATA
#     </h3>
#     </div>

# In[1]:


# Importing all the Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
init_notebook_mode(connected=True)


# In[2]:


df=pd.read_csv('/kaggle/input/top-hits-spotify-from-20002019/songs_normalize.csv')


# In[3]:


df.head()


# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         DATA INFORMATION
#     </h3>
#     </div>

# In[4]:


df.info()


# <div style="color:black;
#             display:fill;
#             border-radius:1px;
#             background-color:lightyellow;
#             font-size:80%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     
# * <b>artist</b>: Name of the Artist.<br>
# * <b>song</b>:   Name of the Track.<br>
# * <b>duration_ms</b>: Duration of the track in milliseconds.<br>
# * <b>explicit</b>: The lyrics or content of a song or a music video contain one or more of the criteria which could be considered offensive or unsuitable for children.<br>
# 
# * <b>year</b>: Release Year of the track.<br>
# * <b>popularity</b>: The higher the value the more popular the song is.<br>
# * <b>danceability</b>: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.<br>
#     
# * <b>energy</b>: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.<br>
# * <b>key</b>: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.<br>
# 
# * <b>loudness</b>: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.<br>
# 
# * <b>mode</b>: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.<br>
# 
# * <b>speechiness</b>: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.<br>
# 
# * <b>acousticness</b>: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.<br>
# 
# * <b>instrumentalness</b>: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.<br>
# 
# * <b>liveness</b>: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.<br>
# 
# * <b>valence</b>: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).<br>
# 
# * <b>tempo</b>: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.<br>
# 
# * <b>genre</b>: Genre of the track.<br>
#     
#     </div>

# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         EXPLORATORY DATA ANALYSIS
#     </h3>
#     </div>

# In[5]:


# checking for null values
df.isnull().sum()


# In[6]:


#checking for duplicate values
df.duplicated().value_counts()


# In[7]:


#dropping the duplicate values
df.drop_duplicates(inplace=True)


# In[8]:


#shape of the dataset
df.shape


# In[9]:


# Description of the Data
df.describe()


# In[10]:


fig=px.imshow(df.corr(),text_auto=True,height=800,width=800,color_continuous_scale=px.colors.sequential.Greens,aspect='auto',title='<b>paiwise correlation of columns')
fig.update_layout(title_x=0.5)
fig.show()


# In[11]:


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


# In[12]:


fig=px.area(df.groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',markers=True,labels={'song':'Total songs'},color_discrete_sequence=['green'],title='<b>Year by Year Songs collection')
fig.update_layout(hovermode='x',title_x=0.5)


# In[13]:


fig=px.histogram(df.groupby('genre',as_index=False).count().sort_values(by='song',ascending=False),x='genre',y='song',color_discrete_sequence=['green'],template='plotly_dark',marginal='box',title='<b>Total songs based on genres</b>')
fig.update_layout(title_x=0.5)


# In[14]:


fig=px.histogram(df.groupby('genre',as_index=False).sum().sort_values(by='popularity',ascending=False),x='genre',y='popularity',color_discrete_sequence=['lightgreen'],template='plotly_dark',marginal='box',title='<b>Popular genres based on pouplarity</b>')
fig.update_layout(title_x=0.5)


# In[15]:


px.bar(df.groupby('artist',as_index=False).count().sort_values(by='song',ascending=False).head(50),x='artist',y='song',labels={'song':'Total Songs'},width=1000,color_discrete_sequence=['green'],text='song',title='<b> List of Songs Recorded by Each Singer')


# In[16]:


px.bar(df.groupby('artist',as_index=False).sum().sort_values(by='popularity',ascending=False).head(30),x='artist',y='popularity',color_discrete_sequence=['lightgreen'],template='plotly_dark',text='popularity',title='<b>Top 30 Popular Singers')


# In[17]:


fig=px.line(df.sort_values(by='popularity',ascending=False).head(25),x='song',y='popularity',hover_data=['artist'],color_discrete_sequence=['green'],markers=True,title='<b> Top 25 songs in Spotify')
fig.show()


# In[18]:


fig=px.treemap(df,path=[px.Constant('Singer'),'artist','genre','song'],values='popularity',title='<b>TreeMap of Singers Playlist')
fig.update_traces(root_color='lightgreen')
fig.update_layout(title_x=0.5)


# In[19]:


fig=px.pie(df.groupby('explicit',as_index=False).count().sort_values(by='song',ascending=False),names='explicit',values='song',labels={'song':'Total songs'},hole=.6,color_discrete_sequence=['green','crimson'],template='plotly_dark',title='<b>Songs having explicit content')
fig.update_layout(title_x=0.5)


# In[20]:


fig=px.area(df[df['explicit']==True].groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',labels={'song':'Total songs'},markers=True,color_discrete_sequence=['red'],template='plotly_dark',title='<b>Yearwise explicit content songs')
fig.update_layout(hovermode='x')


# In[21]:


px.box(df,x='explicit',y='popularity',color='explicit',template='plotly_dark',color_discrete_sequence=['cyan','magenta'],title='<b>popularity based on explicit content')


# In[22]:


px.scatter(df,x='tempo',y='popularity',color='tempo',color_continuous_scale=px.colors.sequential.Plasma,template='plotly_dark',title='<b>Tempo Versus Popularity')


# In[23]:


px.scatter(df,x='speechiness',y='popularity',color='speechiness',color_continuous_scale=px.colors.sequential.Plasma,template='plotly_dark',title='<b> Speechiness Versus Popularity')


# In[24]:


px.scatter(df,x='energy',y='danceability',color='danceability',color_continuous_scale=px.colors.sequential.Plotly3,template='plotly_dark',title='<b>Energy Versus Danceability')


# In[25]:


px.scatter(df,x='energy',y='loudness',color_discrete_sequence=['lightgreen'],template='plotly_dark',title='<b>Energy versus Loudness correlation')


# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         CONCLUSION
#     </h3>
#     </div><br><br>
# <h7>From the Analysis, we can conclude that the most popular genre in the music market is pop. 
# According to the musicians, pop music is inherently popular because it creates a sense of familiarity for listeners. Therefore, when they hear the same 'woop' throughout the genre, they're more inclined to ease into a piece of music they've never heard because it sounds familiar.
# 
# Almost 28% of Songs contains Explicit Content and on coming to popularity, explicit content songs Has high median popularity.
#     
# The top 3 singers who recorded maximum songs in their album are Rihanna, Drake and Eminem. Top 3 popular Singers in Spotify are<br><a href='https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H?autoplay=true' style='text-decoration:none'>Rihanna   </a>,<a href='https://open.spotify.com/artist/7dGJo4pcD2V6oG8kP0tJRR?autoplay=true' style='text-decoration:none'> Eminem</a> and <a href='https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4?autoplay=true' style='text-decoration:none'>Drake </a>.
# 
# Top 3 popular songs to check out are <br><br><a href='https://open.spotify.com/track/5FiHhop5lURiKgpFRHU3QC?autoplay=true' style='text-decoration:none'>1. Sweather Weather</a> by The Neighbourhood<br> <a href='https://open.spotify.com/track/3B8AjxvLomrKgKwWMCNn31?autoplay=true' style='text-decoration:none'>2. Another Love</a> by Tom Odell<br><a href='https://open.spotify.com/track/7lQ8MOhq6IN2w8EYcFNSUk?autoplay=true' style='text-decoration:none'>3. Without Me</a> by Eminem.
# </h7>

# <div style="color:black;
#             display:fill;
#             border-radius:15px;
#             background-color:white;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:black;
#               text-align:center;'>
#         IF LIKED THE NOTEBOOK, PLEASE DO UPVOTE.
#     </h3>
# 
# </div>

# ![](https://i.pinimg.com/originals/88/66/7e/88667eaf29f1bbf12d64abaaeae6caa2.gif)

# <div style="color:white;
#             display:fill;
#             border-radius:15px;
#             background-color:green;
#             font-size:100%;
#             font-family:Verdana;
#             letter-spacing:1px">
#     <h3 style='padding: 20px;
#               color:white;
#               text-align:center;'>
#         END
#     </h3>
#     </div>
