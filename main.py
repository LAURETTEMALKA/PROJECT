import streamlit as st
import pytz
import requests
import datetime as dt

st.title("Today's Weather")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

def display_date_time(zone):
    
    user_time = dt.datetime.now(pytz.timezone(zone))
    formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
    text=(f"Your current date and time in {zone} is: {formatted_user_time}")
    return text


def display_weather(city, unit):
    API = 'e1313973fe262c3c18b4500d98fe65eb'
    url=f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={city}&units={unit}"
    weatherzone = requests.get(url)
    response_weatherzone = weatherzone.json()

    humidity=response_weatherzone['main']['humidity']
    pressure=response_weatherzone['main']['pressure']
    wind=response_weatherzone['wind']['speed']
    description=response_weatherzone['weather'][0]['description']
    temp=response_weatherzone['main']['temp']
    
    a=(f"The weather in {city} is:")
    b=(f'Temperature:', {temp},'°C')
    c=(f'Wind:', {wind})
    d=(f'Pressure:', {pressure})
    e=(f'Humidity:', {humidity})
    f=(f'Description:', {description})
    return a,b,c,d,e,f
    
#def unit_temp(unit):
#    unit_in_api={"Celsius":"metric", "Fahrenheit":"imperial"}
#    unittemp=unit_in_api[unit]
#    return unittemp


location = st.selectbox("Choose a location", pytz.all_timezones)
city = st.text_input("Choose a city", "")
unit_chosen = st.selectbox("Select Temperature Unit: ", ("Celsius", "Fahrenheit"))
unit_in_api = {'Celsius':"metric", 'Fahrenheit':"imperial"}
unittemp = unit_in_api[unit_chosen]
#unit = unit_temp(unit_chosen)


## display date and time and weather for a location
st.write(display_date_time(location))
st.write(display_weather(city,unittemp))

