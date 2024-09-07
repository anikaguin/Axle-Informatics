import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/us-population-2010-2019-reshaped.csv")

df_reshaped = load_data()

# Sidebar
st.sidebar.title("US Population Dashboard")

year_list = list(df_reshaped.year.unique())[::-1]
selected_year = st.sidebar.selectbox("Select Year:", year_list)

color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
selected_color_theme = st.sidebar.selectbox("Select Color Theme:", color_theme_list, index=color_theme_list.index('viridis'))

df_selected_year = df_reshaped[df_reshaped.year == selected_year]
df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

# Helper functions
def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'

def calculate_population_difference(input_df, input_year):
    selected_year_data = input_df[input_df['year'] == input_year].reset_index()
    previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
    selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
    return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

# Gains/Losses
df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

# Main content
st.title(f"US Population Dashboard - {selected_year}")

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Gainer")
    if selected_year > 2010:
        first_state_name = df_population_difference_sorted.states.iloc[0]
        first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
        first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
        st.metric(label=first_state_name, value=first_state_population, delta=f"+ {first_state_delta}")
    else:
        st.write("No data available for 2010")

with col2:
    st.subheader("Top Loser")
    if selected_year > 2010:
        last_state_name = df_population_difference_sorted.states.iloc[-1]
        last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])   
        last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])   
        st.metric(label=last_state_name, value=last_state_population, delta=f"- {last_state_delta}")
    else:
        st.write("No data available for 2010")

# States Migration
st.subheader("States Migration")
col1, col2 = st.columns(2)

if selected_year > 2010:
    df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference > 50000]
    df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]
    
    states_migration_greater = round((len(df_greater_50000)/df_population_difference_sorted.states.nunique())*100)
    states_migration_less = round((len(df_less_50000)/df_population_difference_sorted.states.nunique())*100)
    
    with col1:
        st.metric(label="Inbound Migration", value=f"{states_migration_greater}%")
    with col2:
        st.metric(label="Outbound Migration", value=f"{states_migration_less}%")
else:
    st.write("No migration data available for 2010")

# Choropleth map
st.subheader("Population by State")

def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
    choropleth.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return choropleth

choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
st.plotly_chart(choropleth, use_container_width=True)

# Heatmap
st.subheader("Population Heatmap")

def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    return heatmap

heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
st.altair_chart(heatmap, use_container_width=True)

# Top States
st.subheader("Top States by Population")

max_population = df_selected_year_sorted['population'].max()

for _, row in df_selected_year_sorted.head(10).iterrows():
    col1, col2, col3 = st.columns([2, 6, 2])
    col1.write(row['states'])
    col2.progress(row['population'] / max_population)
    col3.write(f"{row['population']:,}")

# About
st.sidebar.markdown("## About")
st.sidebar.markdown("""
- Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html)
- Gains/Losses: states with high inbound/outbound migration for selected year
- States Migration: percentage of states with annual inbound/outbound migration > 50,000
""")
