from dotenv import load_dotenv 
import os
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')
city = input('Choose a city: ')
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}")

if response.status_code == 404:
    print("City not found. Please check the city name and try again.")
else:
    country = response.json()['sys']['country']
    weather_type = response.json()['weather'][0]['main']
    temperature_farenheit = response.json()['main']['temp']
    temperature_celsium = (temperature_farenheit - 32) * 5/9
    temperature_max = response.json()['main']['temp_max']
    temperature_max_celsium = (temperature_max - 32) * 5/9
    temperature_min = response.json()['main']['temp_min']
    temperature_min_celsium = (temperature_min - 32) * 5/9
    wind_speed_miles = response.json()['wind']['speed']
    wind_speed_km = wind_speed_miles * 1.609344

    result = (f'The weather in {city}, {country} is: {weather_type}\n'
            f'The temperature is: {temperature_celsium:.2f} in °C or {temperature_farenheit} in °F\n'
            f'The max temperature is: {temperature_max_celsium:.2f} in °C or {temperature_max} in °F\n'
            f'The min temperature is: {temperature_min_celsium:.2f} in °C or {temperature_max} in °F\n'
            f'The wind speed is: {wind_speed_km:.2f} in km/h or {wind_speed_miles} in mph')

    print(result)

