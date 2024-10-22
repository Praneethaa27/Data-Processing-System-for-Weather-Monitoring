# Data-Processing-System-for-Weather-Monitoring
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system will utilize data from the OpenWeatherMap API (https://openweathermap.org/).

## Data Source: 
The system will continuously retrieve weather data from the OpenWeatherMap API. You will need to sign up for a free API key to access the data. The API provides various weather parameters, and for this assignment, we will focus on: 

1. **main:** Main weather condition (e.g., Rain, Snow, Clear)

2. **temp:** Current temperature in Centigrade

3. **feels_like:** Perceived temperature in Centigrade

4. **dt:** Time of the data update (Unix timestamp)

## Processing and Analysis: 

1. The system should continuously call the OpenWeatherMap API at a configurable interval (e.g., every 5 minutes) to retrieve real-time weather data for the metros in India. (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad)
2. For each received weather update:

   2.1. Convert temperature values from Kelvin to Celsius (tip : you can also use user preference). 

## Rollups and Aggregates:
1) **Daily Weather Summary:**
- Roll up the weather data for each day.
- Calculate daily aggregates for:

    2.1) Average temperature 

    2.2) Maximum temperature 

    2.3) Minimum temperature 

    2.4) Dominant weather condition (give reason on this) 

  Store the daily summaries in a database or persistent storage for further analysis. 
  
2) **Alerting Thresholds:**

- Define user-configurable thresholds for temperature or specific weather conditions (e.g., alert if temperature exceeds 35 degrees Celsius for two consecutive updates).
- Continuously track the latest weather data and compare it with the thresholds.
- If a threshold is breached, trigger an alert for the current weather conditions. Alerts could be displayed on the console or sent through an email notification system (implementation details left open-ended).

3) **Implement visualizations:**

- To display daily weather summaries, historical trends, and triggered alerts.

## Test Cases: 
1) **System Setup:** 
- Verify system starts successfully and connects to the OpenWeatherMap API using a valid API key. 
2) **Data Retrieval:**
- Simulate API calls at configurable intervals. 
- Ensure the system retrieves weather data for the specified location and parses the response correctly. 
3) **Temperature Conversion:** 
- Test conversion of temperature values from Kelvin to Celsius (or Fahrenheit) based on user preference. 
4) **Daily Weather Summary:**
- Simulate a sequence of weather updates for several days.
- Verify that daily summaries are calculated correctly, including average, maximum, minimum temperatures,and dominant weather condition. 
5) **Alerting Thresholds:**
- Define and configure user thresholds for temperature or weather conditions.
- Simulate weather data exceeding or breaching the thresholds.
- Verify that alerts are triggered only when a threshold is violated.

## Bonus: 
- Extend the system to support additional weather parameters from the OpenWeatherMap API (e.g., humidity, wind speed) and incorporate them into rollups/aggregates.
- Explore functionalities like weather forecasts retrieval and generating summaries based on predicted conditions.


# Steps:
## File Structure
weather_monitoring_system/

├── app.py                       # Main application file

├── config.py                    # Configuration file (API key, cities, etc.)

├── data_processing.py            # Data processing, rollups, and aggregate functions

├── alert_system.py               # Alerting and threshold monitoring

├── visualization.py              # Code for creating visualizations

├── test_cases.py                 # Test cases for the system

├── requirements.txt              # Python dependencies

└── data/
      └── daily_weather_summary.csv  # CSV file to store daily weather summaries

![Screenshot 2024-10-22 113709](https://github.com/user-attachments/assets/c5a7308c-666d-4a8b-84f8-625d96ac3737)


## Tools & Technologies

•**Language**: Python

•**Database**: SQLite or CSV files (for lightweight persistence)

•**API Integration**: OpenWeatherMap API

•**Visualization**: Matplotlib or Plotly

•**Alerting**: Email (optional) or console notifications

•**Test Framework**: Python’s built-in unittest

## Step-by-Step Instructions

**Step 1**: Create *requirements.txt* for Dependencies

First, create a *requirements.txt* file to manage dependencies. This will make it easy for others to install necessary packages. 

You can install these dependencies using: 

  *pip install -r requirements.txt*
  
**Step 2**: Create *config.py* for Configurations

This file will store API keys, city names, and other configurations.

Get API_KEY from [Openweathermap](https://home.openweathermap.org/api_keys)

![image](https://github.com/user-attachments/assets/6d0b391d-53ba-42c1-9dc8-6753f8b5b0f9)


**Step 3**: Create *data_processing.py* for Data Handling

This file will handle retrieving weather data, converting temperatures, and calculating aggregates.

**Step 4**: Create *alert_system.py* for Alerts

This module monitors the data and triggers alerts based on user-defined thresholds.

**Step 5**: Create *visualization.py* for Data Visualization

This file creates visualizations like daily temperature trends and alert history.

**Step 6**: Create *app.py* to Run the Main Application

This is the main file that orchestrates the API calls, data processing, and alerting.

**Step 7**: Create *test_cases.py* for Unit Tests

This file will test different functionalities of the system.

## Run tests using:

 *python test_cases.py*
 
### How to Run the System

  **1.Install dependencies:**
  
  *pip install -r requirements.txt*
 
 **2.Set up the API key in  *config.py*.** 
 
 **3.Run the main application:**
 
 *python app.py*

**4.Run tests:**

*python test_cases.py*

**5.Visualize the data by running:**

*python visualization.py*

By following these steps, you'll have a fully functioning real-time weather monitoring system complete with API integration, data rollups, alerts, and visualizations.

# Result

**Date**: *22-10-2024*
**Time:** *AT 10:55 AM*

![image](https://github.com/user-attachments/assets/fbd76a67-6bba-4df6-a5e8-58ea874a43c6)

**Date**: *22-10-2024*
**Time:** *AT 11:45 AM*
![image](https://github.com/user-attachments/assets/68649c6b-9aef-4eb5-83dd-bd29d53ac019)

**Date**: *22-10-2024*
**Time:** *AT 15:42 PM*
<img alt="image" src="https://github.com/user-attachments/assets/ea20c5d4-9edd-4928-83f8-5b1609106222">
