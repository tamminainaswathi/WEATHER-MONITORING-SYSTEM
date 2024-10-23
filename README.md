Weather Monitoring System


This project is a Real-Time Weather Monitoring System that utilizes data from the OpenWeatherMap API to gather weather information for multiple cities. The system performs rollups and aggregates on the data,triggers alerts when thresholds are crossed, and visualizes weather trends over time.

Key Features

- Real-Time Weather Data: Fetches current weather data (temperature, weather conditions) for predefined cities.

Daily Weather Summaries:
- Rolls up the weather data for each day.

Aggregates include:
- Average temperature
- Maximum temperature
- Minimum temperature

Alerting Thresholds:
- Configurable thresholds for temperature (alert if the temperature exceeds 30°C).
- Alerts are triggered based on these thresholds and can be displayed or sent through a notification system.

Visualizations:
- Provides graphs for daily summaries and weather trends.

Prerequisites
- Python 3.x
- pip
- OpenWeatherMap API Key

To Access The Application:
 - http://127.0.0.1:5000/get_weather_data

