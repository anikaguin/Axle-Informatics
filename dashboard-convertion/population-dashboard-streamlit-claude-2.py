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

# Main content
st.title(f"US Population Dashboard - {selected_year}")

# Gains/Losses
df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Highest Population Gain")
    if selected_year > 2010:
        first_state_name = df_population_difference_sorted.states.iloc[0]
        first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
        first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
        st.write(f"**{first_state_name}**")
        st.write(f"Population: {first_state_population}")
        st.write(f"Delta: + {first_state_delta}")
    else:
        st.write("No data available for 2010")

with col2:
    st.subheader("Highest Population Loss")
    if selected_year > 2010:
        last_state_name = df_population_difference_sorted.states.iloc[-1]
        last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])   
        last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])   
        st.write(f"**{last_state_name}**")
        st.write(f"Population: {last_state_population}")
        st.write(f"Delta: {last_state_delta}")
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
else:
    states_migration_greater = 0
    states_migration_less = 0

with col1:
    st.metric("Inbound Migration", f"{states_migration_greater}%")

with col2:
    st.metric("Outbound Migration", f"{states_migration_less}%")

# Choropleth map
st.subheader("Population Distribution")
fig = px.choropleth(df_selected_year, locations='states_code', color='population', locationmode="USA-states",
                    color_continuous_scale=selected_color_theme,
                    range_color=(0, max(df_selected_year.population)),
                    scope="usa",
                    labels={'population':'Population'})
fig.update_layout(height=350, margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig, use_container_width=True)

# Heatmap
st.subheader("Population Heatmap")
heatmap = alt.Chart(df_reshaped).mark_rect().encode(
    y=alt.Y('year:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
    x=alt.X('states:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
    color=alt.Color('max(population):Q', scale=alt.Scale(scheme=selected_color_theme), legend=None),
    stroke=alt.value('black'),
    strokeWidth=alt.value(0.25),
).properties(width=900).configure_axis(labelFontSize=12, titleFontSize=12)
st.altair_chart(heatmap, use_container_width=True)

# Top States
st.subheader("Top States by Population")
for _, row in df_selected_year_sorted.head(10).iterrows():
    state = row['states']
    population = row['population']
    st.write(f"{state}: {population:,}")

# About
st.sidebar.markdown("## About")
st.sidebar.markdown("""
- Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html)
- Gains/Losses: states with high inbound/outbound migration for selected year
- States Migration: percentage of states with annual inbound/outbound migration > 50,000
""")
