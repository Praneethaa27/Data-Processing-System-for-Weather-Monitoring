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

**Step 1**: Create requirements.txt for Dependencies

First, create a *requirements.txt* file to manage dependencies. This will make it easy for others to install necessary packages. 

You can install these dependencies using: 

  *pip install -r requirements.txt*

Get API_KEY from [Openweathermap](https://home.openweathermap.org/api_keys)

![image](https://github.com/user-attachments/assets/6d0b391d-53ba-42c1-9dc8-6753f8b5b0f9)




