import datetime
import streamlit as st

t = st.time_input("Set an alarm:", datetime.time(8, 45))
st.write("Alarm is set for", t)
