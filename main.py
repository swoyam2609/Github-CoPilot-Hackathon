import pandas as pd
import requests

wind_directions = {
        'N': (348.75, 11.25),
        'NNE': (11.25, 33.75),
        'NE': (33.75, 56.25),
        'ENE': (56.25, 78.75),
        'E': (78.75, 101.25),
        'ESE': (101.25, 123.75),
        'SE': (123.75, 146.25),
        'SSE': (146.25, 168.75),
        'S': (168.75, 191.25),
        'SSW': (191.25, 213.75),
        'SW': (213.75, 236.25),
        'WSW': (236.25, 258.75),
        'W': (258.75, 281.25),
        'WNW': (281.25, 303.75),
        'NW': (303.75, 326.25),
        'NNW': (326.25, 348.75)
    }

def get_wind_direction(degree):
    for direction, (lower, upper) in wind_directions.items():
        if lower <= degree < upper:
            return direction

apikey = "b6bd5446692494490688ce6b30036430"

def currentData(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(
        city, 'metric', apikey)
    resp = requests.get(url)
    result = resp.json()

    weather = result['weather'][0]['main']
    currentTemp = result['main']['temp']
    minTemp = result['main']['temp_min']
    maxTemp = result['main']['temp_max']
    feelTemp = result['main']['feels_like']
    pressure = result['main']['pressure']
    humidity = result['main']['humidity']
    windSpeed = result['wind']['speed']
    windDirection = get_wind_direction(result['wind']['deg'])


    print("The current weather in {} is: {}".format(city, weather))
    print()
    print("The current temperature is: {}".format(
        u"{}\u00b0".format(currentTemp)))
    print("The temperature feels like: {}".format(u"{}\u00b0".format(feelTemp)))
    print("The minimum temperature of the day is expected to be: {}".format(
        u"{}\u00b0".format(minTemp)))
    print("The maximum temperature of the day is expected to be: {}".format(
        u"{}\u00b0".format(maxTemp)))
    print()
    print("The air pressure in {} is: ".format(city), pressure, "hPa")
    print("The humidity in {} is: {}%".format(city, humidity))
    print()
    print("The Wind Speed and its direction is: {}m/s {}".format(windSpeed, windDirection))
    print("\n")

cityName = input("Enter the City name: ")

print("\n")

print("What kind of Forcast you want to recieve: ")
print("1. Current Weather Data")
print("2. Hourly Forecast for 4 Days")
print("3. Daily forecast for 16 Days")
print("4. Climatic Forecast for 30 Days")

print("\n")

a = int(input("Enter your input: "))

print("\n")

if (a == 1):
    currentData(cityName)
