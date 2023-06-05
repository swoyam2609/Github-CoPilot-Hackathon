import requests
import json

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

def getWindDirection(degree):
    for direction, (lower, upper) in wind_directions.items():
        if lower <= degree < upper:
            return direction
        
apiKey = input("Enter your API Key: ")

def getCurrentWeather(cityName):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(cityName, 'metric', apiKey)
    response = requests.get(url)

    # If response if 404, then city is not found
    if response.status_code == 404:
        print("City not found")
        return
    
    # If response is 401, then API key is invalid
    if response.status_code == 401:
        print("Invalid API Key")
        return
    
    # If response is 200, then city is found
    result = response.json()

    weather = result['weather'][0]['main']
    currentTemp = result['main']['temp']
    minTemp = result['main']['temp_min']
    maxTemp = result['main']['temp_max']
    feelTemp = result['main']['feels_like']
    pressure = result['main']['pressure']
    humidity = result['main']['humidity']
    windSpeed = result['wind']['speed']
    windDirection = getWindDirection(result['wind']['deg'])

    print("The current weather in {} is: {}".format(cityName, weather))
    print("The current temperature is: {}".format(u"{}\u00b0".format(currentTemp)))
    print("The temperature feels like: {}".format(u"{}\u00b0".format(feelTemp)))
    print("The minimum temperature of the day is expected to be: {}".format(u"{}\u00b0".format(minTemp)))
    print("The maximum temperature of the day is expected to be: {}".format(u"{}\u00b0".format(maxTemp)))
    print("The air pressure in {} is: ".format(cityName), pressure, "hPa")
    print("The humidity in {} is: {}%".format(cityName, humidity))
    print("The wind speed in {} is: {} m/s".format(cityName, windSpeed))
    print("The wind direction in {} is: {}".format(cityName, windDirection))

cityName = input("Enter the name of the city: ")
getCurrentWeather(cityName)