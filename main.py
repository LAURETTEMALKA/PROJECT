
import streamlit as st
import pytz
import requests
import datetime as dt

zone= st.selectbox("Choose a city", pytz.all_timezones)

## display date and time for a location
st.subheader(yw.display_date_time_weather(zone))
