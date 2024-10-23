import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui.plotter import plot_weather_trends

# Mock weather data for testing
daily_summary = {
    '2024-10-20': {'avg_temp': 25},
    '2024-10-21': {'avg_temp': 26},
    '2024-10-22': {'avg_temp': 28},
    '2024-10-23': {'avg_temp': 27},
    '2024-10-24': {'avg_temp': 30}
}

# Call the function to plot the data
plot_weather_trends(daily_summary)
