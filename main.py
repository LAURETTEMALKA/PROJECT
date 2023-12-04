import streamlit as st
import pytz
import requests
import datetime as dt

zone = st.selectbox("Choose a city", pytz.all_timezones)

## display date and time and weather for a location
st.subheader(weather.display_date_time_weather())

def display_date_time_weather(zone="Israel"):
    user_time = dt.datetime.now(pytz.timezone(zone))
    formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
    print(f"Your current date and time in {zone}: {formatted_user_time}")

    #a=[]
    #for zone in pytz.all_timezones:
    #    zone_separated = zone.split("/")
    #    city=zone_separated[len(zone_separated)-1]
    #    a.append(city)

    zone_separated = zone.split("/")
    city=zone_separated[len(zone_separated)-1]  
    print(f"The weather in {city}:")  

    API = 'e1313973fe262c3c18b4500d98fe65eb'
    url=f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={city="Jerusalem"}"
    weatherzone = requests.get(url)
    response_weatherzone = weatherzone.json()

    humidity=response_weatherzone['main']['humidity']
    pressure=response_weatherzone['main']['pressure']
    wind=response_weatherzone['wind']['speed']
    description=response_weatherzone['weather'][0]['description']
    temp=response_weatherzone['main']['temp']

    print(f'Temperature:', {temp},'°C')
    print(f'Wind:', {wind})
    print(f'Pressure:', {pressure})
    print(f'Humidity:', {humidity})
    print(f'Description:', {description})
