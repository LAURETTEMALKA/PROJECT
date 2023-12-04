
import streamlit as st
import pytz
import requests
import datetime as dt

zone= st.selectbox("Choose a city", pytz.all_timezones)

## display date and time for a location
date_time_weather=display_date_time_weather(zone)
st.subheader(date_time_weather)
