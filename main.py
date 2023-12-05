import streamlit as st
import pytz
import requests
import datetime as dt
import pandas as pd
from skimage import io


st.title("Today's Date, Time and Weather")
st.write("## *Made by Laurette*")
st.write("##")

#st.write("### You have to full all this empty cases")

def display_date_time(zone='Israel'):
    
    user_time = dt.datetime.now(pytz.timezone(zone))
    formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
    #text=(f"Your current date and time in {zone} is: \n {formatted_user_time}")
    text=(f"### *{formatted_user_time}*")
    return text


def display_weather(city="Jerusalem", unit="metric"):
    API = 'e1313973fe262c3c18b4500d98fe65eb'
    url=f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={city}&units={unit}"
    weatherzone = requests.get(url)
    response_weatherzone = weatherzone.json()

    humidity=response_weatherzone['main']['humidity']
    pressure=response_weatherzone['main']['pressure']
    wind=response_weatherzone['wind']['speed']
    description=response_weatherzone['weather'][0]['description']
    temp=response_weatherzone['main']['temp']
    icon_code = response_weatherzone["weather"][0]["icon"]
    icon_url = io.imread(f"https://openweathermap.org/img/wn/{icon_code}@2x.png")
    #icon = icon_url
    
    a=f"The weather in {city} is:"
    b=f'Temperature: {temp},°C'
    #c=f'Wind: {wind}'
    c= st.write(f"### 💨 Wind Speed: {wind} m/s")
    #d=f'Pressure: {pressure}'
    d = st.write(f"### ⏲️ Pressure: {pressure} mBar")
    #e=f'Humidity: {humidity}'
    e = st.write(f"### 💧 Humidity: {humidity} %")
    #f=f'Description: {description}'
    f = st.write(f"### {icon_url} Description: {description}")
    return a, b, c, d, e, f

def unit_temp(unit):
    unit_in_api={"Celsius":"metric", "Fahrenheit":"imperial"}
    unittemp=unit_in_api[unit]
    return unittemp

st.write("## Date and time in Israel:")
st.write(display_date_time())

st.write("## The weather in Jerusalem:")
st.write(display_weather())



st.write("### Choose the zone of your location in this list to display date and time :")
location = st.selectbox("Choose a location", pytz.all_timezones)
st.write(f" ## We are in {location} area: ")
st.write(display_date_time(location))

st.write("### Write the name of the city you are interested in to display the weather:")
city = st.text_input("Choose a city", "")
st.write("### Choose the unit for the temperature of the weather")
unit_chosen = st.selectbox("Select Temperature Unit: ", ("Celsius", "Fahrenheit"))
#unit_in_api = {'Celsius':"metric", 'Fahrenheit':"imperial"}
#unittemp = unit_in_api[unit_chosen]
unit = unit_temp(unit_chosen)
st.write(display_weather(city,unit))



# table
on = st.toggle(f"Show weather details of ***{city}***")

if on:
    df = pd.DataFrame(display_weather(selected_value))
    df
