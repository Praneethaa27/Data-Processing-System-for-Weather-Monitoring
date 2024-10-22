# Weather Monitoring System: Summary

The system retrieves real-time weather data from OpenWeatherMap API for multiple cities, calculates daily weather summaries, 
provides weather forecasts, and triggers alerts based on specific weather conditions. The system is built with several modular 
components that handle different aspects of data retrieval, processing, and alerting.

## Core Files and Their Roles

### 1. app.py:

This is the main orchestration file that runs the system and controls the following:

- Fetches real-time weather data for a list of cities using *get_weather_data()*.
- Calculates and saves daily weather summaries using *calculate_daily_aggregates()* and *save_daily_summary()*.
- Fetches weather forecasts for the next 5 days using *get_weather_forecast()*.
- Checks for weather alerts based on extreme weather conditions using *check_alerts()*.
- Polls the OpenWeatherMap API periodically (e.g., every hour) as defined in the configuration.


### 2. data_processing.py:
This module processes the weather data and aggregates it for reporting and summarization.

- **get_weather_data(city)**: Retrieves real-time weather parameters such as temperature, humidity, wind speed, and weather description.
- **calculate_daily_aggregates(weather_data)**: Aggregates data for the day and computes averages for parameters like temperature, humidity, and wind speed.
- **get_weather_forecast(city)**: Fetches a 5-day weather forecast including temperature, humidity, and wind speed for a city.
- **generate_forecast_summary(forecast_data)**: Computes averages of forecasted weather parameters and summarizes the predicted weather conditions.
- **save_daily_summary(summary)**: Saves the daily weather summaries (can be customized based on the saving mechanism, e.g., file, database).


### 3. alert_system.py:
This file handles the logic for generating alerts based on weather data.

- **check_alerts(weather_data)**: This function checks the weather parameters for specific thresholds (temperature, humidity, wind speed) and triggers alerts for:

-- High temperatures (above 35°C).
  
-- High humidity (above 80%).

-- Strong winds (wind speed above 20 m/s).

-- Cold temperatures (below 0°C).

-- Alerts are printed in the console and can easily be extended to other notification systems like email, SMS, etc.

### 4. config.py:
This file contains all the configuration settings needed by the system.

- **API_KEY**: The OpenWeatherMap API key for making requests.
- **CITIES**: A list of cities for which weather data is retrieved. You can easily add or remove cities from this list.
- **POLL_INTERVAL**: Defines how frequently the system should poll the API for new weather data (in seconds).


### 5. requirements.txt:
Contains dependencies for the system:
- *requests*: The Python library used to make HTTP requests to the OpenWeatherMap API.

## New Features in the Extended System

1. **Additional Weather Parameters**:

The system now retrieves and processes additional weather parameters:

- **Humidity**: Monitored for discomfort alerts and included in summaries.
- **Wind Speed**: Tracked for generating high wind alerts and summaries.
- **Weather Description**: Provides a textual description of current weather conditions.


2. **Forecasting and Summarization**:

The system now retrieves 5-day weather forecasts for each city:

- Forecast data includes temperature, humidity, wind speed, and descriptions.
- **Summaries** are generated based on predicted conditions to give an average view of the weather trends in the coming days.

3. **Daily Aggregates**:

The system aggregates daily weather data for each city, calculating:
- Average Temperature.
- Average Humidity.
- Average Wind Speed.

  
This helps users to understand weather trends and variations over time.

4. **Alerts for Extreme Weather**:

Alerts are triggered if certain thresholds are crossed:

- **Heat alerts**: Triggered if temperature exceeds 35°C.
- **High humidity alerts**: Triggered if humidity exceeds 80%.
- **Strong wind alerts**: Triggered if wind speed exceeds 20 m/s.
- **Cold weather alerts**: Triggered if the temperature drops below 0°C.


## Example Workflow
1. **Start the Application:**
- The app fetches real-time weather data for all cities in the CITIES list.
- The system calculates and prints daily aggregates.
- If any extreme conditions are detected, alerts are printed.
  
2. **Forecast Summaries:**

- The system retrieves 5-day forecasts and prints out summaries of predicted conditions.

3. **Repeat:**
- After the set interval *(POLL_INTERVAL)*, the system fetches fresh data and repeats the process.


## Use Cases
- **Weather Monitoring for Multiple Cities**: Keep track of weather conditions across multiple cities, useful for global weather tracking.
- **Extreme Weather Alerts**: Immediate notifications when thresholds for temperature, humidity, or wind speed are crossed.
- **Weather Forecasting**: Access to summarized weather forecasts for planning purposes based on predictions for the next 5 days.

## Customizations
1. **Add/Remove Cities**: Modify the **CITIES** list in *config.py* to monitor different locations.
2. **Modify Alert Thresholds**: Adjust thresholds in *alert_system.py* to suit different weather conditions based on specific needs.
3. **Change Polling Frequency**: Adjust **POLL_INTERVAL** to control how often data is refreshed.

