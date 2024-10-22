# alert_system.py

def check_alerts(weather_data, temp_threshold=35):
    consecutive_exceeds = 0
    for record in weather_data:
        if record['temp_celsius'] > temp_threshold:
            consecutive_exceeds += 1
            if consecutive_exceeds >= 2:
                trigger_alert(record['city'], record['temp_celsius'])
        else:
            consecutive_exceeds = 0

def trigger_alert(city, temperature):
    print(f"ALERT: {city} has exceeded {temperature}°C for two consecutive updates!")
    # Optional: Send email using smtplib if required
