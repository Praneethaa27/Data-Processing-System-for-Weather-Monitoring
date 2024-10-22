# data_processing.py

import requests # type: ignore
import pandas as pd # type: ignore
from config import API_KEY, BASE_URL, CITIES

# Function to retrieve weather data
def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    temp_kelvin = data['main']['temp']
    weather_condition = data['weather'][0]['main']
    timestamp = data['dt']
    return {
        'city': city,
        'temp_celsius': kelvin_to_celsius(temp_kelvin),
        'weather_condition': weather_condition,
        'timestamp': timestamp
    }

# Temperature conversion
def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Function to roll up daily data into aggregates
def calculate_daily_aggregates(weather_data):
    df = pd.DataFrame(weather_data)
    daily_summary = {
        'average_temp': df['temp_celsius'].mean(),
        'max_temp': df['temp_celsius'].max(),
        'min_temp': df['temp_celsius'].min(),
        'dominant_condition': df['weather_condition'].mode()[0]
    }
    return daily_summary

# Function to store the summary in a CSV file
def save_daily_summary(summary, file_path="data/daily_weather_summary.csv"):
    df = pd.DataFrame([summary])
    df.to_csv(file_path, mode='a', header=not pd.io.common.file_exists(file_path), index=False)
