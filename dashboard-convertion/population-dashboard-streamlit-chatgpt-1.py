import pandas as pd
import plotly.express as px
import altair as alt
import streamlit as st

# Load data
df_reshaped = pd.read_csv("data/us-population-2010-2019-reshaped.csv")

# Dropdowns
year_list = list(df_reshaped.year.unique())[::-1]
color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']

st.sidebar.header("Settings")
selected_year = st.sidebar.selectbox("Select Year:", year_list)
selected_color_theme = st.sidebar.selectbox("Select Color Theme:", color_theme_list)

# Data Filtering
df_selected_year = df_reshaped[df_reshaped.year == selected_year]
df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

# Utility Functions
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

df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

# Top/Bottom States
if selected_year > 2010:
    first_state_name = df_population_difference_sorted.states.iloc[0]
    first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
    first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
else:
    first_state_name = '-'
    first_state_population = '-'
    first_state_delta = ''

if selected_year > 2010:
    last_state_name = df_population_difference_sorted.states.iloc[-1]
    last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])
    last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])
else:
    last_state_name = '-'
    last_state_population = '-'
    last_state_delta = ''

# Display Metrics
st.metric(label="State with Highest Population Gain", value=f"{first_state_name}", delta=f"+{first_state_delta}")
st.metric(label="State with Highest Population Loss", value=f"{last_state_name}", delta=f"{last_state_delta}")

# Donut Chart
def make_donut(input_response, input_text, input_color):
    chart_color = {
        'blue': ['#29b5e8', '#155F7A'],
        'green': ['#27AE60', '#12783D'],
        'orange': ['#F39C12', '#875A12'],
        'red': ['#E74C3C', '#781F16']
    }.get(input_color, ['#29b5e8', '#155F7A'])

    source = pd.DataFrame({"Topic": ['', input_text], "% value": [100 - input_response, input_response]})
    source_bg = pd.DataFrame({"Topic": ['', input_text], "% value": [100, 0]})

    plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color=alt.Color("Topic:N", scale=alt.Scale(domain=[input_text, ''], range=chart_color), legend=None)
    ).properties(width=130, height=130)

    text = plot.mark_text(align='center', font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
    plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
        theta="% value",
        color=alt.Color("Topic:N", scale=alt.Scale(domain=[input_text, ''], range=chart_color), legend=None)
    ).properties(width=130, height=130)

    return plot_bg + plot + text

# States Migration
if selected_year > 2010:
    df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference > 50000]
    df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]

    states_migration_greater = round((len(df_greater_50000) / df_population_difference_sorted.states.nunique()) * 100)
    states_migration_less = round((len(df_less_50000) / df_population_difference_sorted.states.nunique()) * 100)

    st.altair_chart(make_donut(states_migration_greater, 'Inbound Migration', 'green'))
    st.altair_chart(make_donut(states_migration_less, 'Outbound Migration', 'red'))
else:
    st.altair_chart(make_donut(0, 'Inbound Migration', 'green'))
    st.altair_chart(make_donut(0, 'Outbound Migration', 'red'))

# Choropleth Map
def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population': 'Population'})
    choropleth.update_layout(
        template='plotly_dark',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth

st.plotly_chart(make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme))

# Heatmap
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
        y=alt.Y(f'{input_y}:O'),
        x=alt.X(f'{input_x}:O'),
        color=alt.Color(f'max({input_color}):Q', scale=alt.Scale(scheme=input_color_theme), legend=None)
    ).properties(width=900)
    return heatmap

st.altair_chart(make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme))

# About Section
st.sidebar.subheader("About")
st.sidebar.markdown("""
- Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html)
- Gains/Losses: States with high inbound/outbound migration for selected year.
- States Migration: Percentage of states with annual inbound/outbound migration > 50,000.
""")
