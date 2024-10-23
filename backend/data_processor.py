# backend/data_processor.py
import statistics
from datetime import datetime

def process_weather_data(weather_data):
    daily_summary = {}
    
    for data in weather_data:
        city = data['city']
        temp_celsius = data['temp'] - 273.15  # Convert from Kelvin to Celsius
        weather = data['weather']
        dt = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d')

        if dt not in daily_summary:
            daily_summary[dt] = {
                'temps': [],
                'weathers': [],
                'max_temp': None,
                'min_temp': None
            }
        
        daily_summary[dt]['temps'].append(temp_celsius)
        daily_summary[dt]['weathers'].append(weather)
        daily_summary[dt]['max_temp'] = max(daily_summary[dt]['temps'])
        daily_summary[dt]['min_temp'] = min(daily_summary[dt]['temps'])

    for day, summary in daily_summary.items():
        summary['avg_temp'] = statistics.mean(summary['temps'])
        summary['dominant_weather'] = max(set(summary['weathers']), key=summary['weathers'].count)

    return daily_summary
