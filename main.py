import streamlit as st
import pytz
import requests
import datetime as dt
import weather_app.py

zone = st.selectbox("Choose a city", pytz.all_timezones)

## display date and time for a location
st.subheader(weather_app.display_date_time_weather(zone))
