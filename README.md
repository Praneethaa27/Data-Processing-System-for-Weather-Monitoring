# Data-Processing-System-for-Weather-Monitoring
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system will utilize data from the OpenWeatherMap API (https://openweathermap.org/).


# Solution:
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
