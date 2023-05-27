# Weather Data Script

This Python script retrieves weather data using the OpenWeatherMap API based on user input for the API key and city name. It provides information such as the current weather, temperature, pressure, humidity, and wind details.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your machine
- pandas library installed (you can install it using pip install pandas)
- An OpenWeatherMap API key. If you don't have one, you can sign up for free at OpenWeatherMap and obtain an API key.
## Usage

- Clone or download the script to your local machine.
- Open a terminal or command prompt and navigate to the directory where the script is located.
- Run the script using the command 
```py
python3 main.py
```
- You will be prompted to enter your OpenWeatherMap API key. Provide the key and press Enter.
- Next, enter the name of the city for which you want to retrieve weather data and press Enter.
- Choose the type of forecast you want to receive by entering the corresponding number and pressing Enter:
  - 1: Current Weather Data
  - 2: Hourly Forecast for 4 Days
  - 3: Daily Forecast for 16 Days
  - 4: Climatic Forecast for 30 Days
- The script will fetch the weather data and display it on the console.

Note: The script uses the requests library to make API requests and the pandas library for data manipulation. Make sure you have these libraries installed.

Feel free to modify the script according to your needs or integrate it into your projects.

If you have any questions or encounter any issues, please let me know.