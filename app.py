# app.py

import time
from data_processing import get_weather_data, calculate_daily_aggregates, save_daily_summary
from alert_system import check_alerts
from config import CITIES, POLL_INTERVAL

def main():
    weather_data = []
    while True:
        for city in CITIES:
            data = get_weather_data(city)
            weather_data.append(data)
            print(f"Retrieved weather data for {city}: {data['temp_celsius']}°C")
        
        # After collecting all cities' data, process daily aggregates
        daily_summary = calculate_daily_aggregates(weather_data)
        save_daily_summary(daily_summary)
        
        # Check for any alerts
        check_alerts(weather_data)
        
        # Wait before next API call
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
