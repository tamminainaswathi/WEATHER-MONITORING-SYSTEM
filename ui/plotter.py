# ui/plotter.py

import matplotlib.pyplot as plt

def plot_weather_trends(daily_summary):
    dates = list(daily_summary.keys())
    avg_temps = [summary['avg_temp'] for summary in daily_summary.values()]
    
    plt.plot(dates, avg_temps, marker='o', label='Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Weather Summary')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
