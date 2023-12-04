import weather_app.py as wa
import streamlit as st
import pytz
import requests
import datetime as dt

zone= st.selectbox("Choose a city", pytz.all_timezones)

## display date and time for a location
st.write(wa.display_date_time_weather(zone))
