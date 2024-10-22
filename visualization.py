# visualization.py

import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

def plot_weather_trends(file_path="data/daily_weather_summary.csv"):
    df = pd.read_csv(file_path)
    df.plot(x='date', y=['average_temp', 'max_temp', 'min_temp'], kind='line')
    plt.title("Daily Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.show()
