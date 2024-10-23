from flask import Flask, jsonify
import requests
from collections import defaultdict

app = Flask(__name__)

API_KEY = '1381971191c42ae649a487326ae7082c'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad','Tirupati']
ALERT_THRESHOLD = 30  
daily_summary = defaultdict(dict)

# Function to calculate aggregate values
def calculate_daily_aggregates(weather_data):
    for city, city_weather in weather_data.items():
        avg_temp = sum(city_weather['temps']) / len(city_weather['temps'])
        max_temp = max(city_weather['temps'])
        min_temp = min(city_weather['temps'])
        dominant_weather = max(set(city_weather['weathers']), key=city_weather['weathers'].count)

        daily_summary[city] = {
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_weather': dominant_weather
        }

        # Trigger alert if the max temperature exceeds the threshold
        if max_temp > ALERT_THRESHOLD:
            print(f"Alert: {city} exceeded the temperature threshold of {ALERT_THRESHOLD}°C!")

@app.route('/get_weather_data', methods=['GET'])
def get_weather_data():
    weather_data = defaultdict(lambda: {'temps': [], 'weathers': []})  # Dictionary to store city data
    result = []

    for city in cities:
        try:
            url = BASE_URL.format(city, API_KEY)
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            data = response.json()

            if 'main' in data:
                temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
                weather_condition = data['weather'][0]['main']

                # Append city weather data to our weather_data dictionary
                weather_data[city]['temps'].append(temp)
                weather_data[city]['weathers'].append(weather_condition)

                result.append({
                    'city': city,
                    'temp': temp,
                    'feels_like': data['main']['feels_like'] - 273.15,  # Convert feels_like to Celsius
                    'weather': weather_condition,
                    'dt': data['dt']
                })
            else:
                result.append({
                    'city': city,
                    'error': data.get('message', 'No weather data available')
                })
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")
            return jsonify({'error': str(e)}), 500

    # Calculate and store daily summaries and aggregates
    calculate_daily_aggregates(weather_data)

    return jsonify(result)

@app.route('/daily_summary', methods=['GET'])
def get_daily_summary():
    return jsonify(daily_summary)

if __name__ == '__main__':
    app.run(debug=True)
