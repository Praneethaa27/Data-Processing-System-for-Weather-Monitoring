# alert_system.py

# Function to check for alerts based on weather conditions
def check_alerts(weather_data):
    for data in weather_data:
        city = data['city']
        temp = data['temp_celsius']
        humidity = data['humidity']
        wind_speed = data['wind_speed']

        # Temperature alert
        if temp > 35:
            print(f"⚠️ Heat alert in {city}: {temp}°C. Stay hydrated and avoid outdoor activities.")

        # Humidity alert
        if humidity > 80:
            print(f"⚠️ High humidity alert in {city}: {humidity}%. This may cause discomfort and heat-related illnesses.")

        # Wind speed alert
        if wind_speed > 20:
            print(f"⚠️ High wind speed alert in {city}: {wind_speed} m/s. Secure loose objects and be cautious.")

        # Cold temperature alert
        if temp < 0:
            print(f"❄️ Cold weather alert in {city}: {temp}°C. Dress warmly and stay indoors if possible.")

