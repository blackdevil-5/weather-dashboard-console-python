#This module is used create presentation for weather report
import matplotlib.pyplot as plt
from storage import WeatherStore

class WeatherVisual:
    def __init__(self, data_file="weather_data.json"):
        self.storage = WeatherStore(data_file)

    def plot_temperature_trend(self, city):
        data = self.storage.load_data()

        city = city.lower()
        city_data = [entry for entry in data if entry["city"].lower() == city]

        if len(city_data) < 2:
            print(f"Not enough data to plot temperature trend for {city.title()}. Please fetch data multiple times.")
            return

        dates = [entry["date"] for entry in city_data]
        temps = [entry["temperature"] for entry in city_data]

        plt.figure()
        plt.plot(dates, temps, marker='o')
        plt.title(f"Temperature Trend for {city.title()}")
        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def plot_city_comparison(self):
        data = self.storage.load_data()

        if len(data) < 2:
            print("Not enough data to compare cities. Please fetch more data.")
            return

        # Get latest data entries for each city (by latest date)
        latest_entries = {}
        for entry in reversed(data):  # Reversed so latest comes first
            city = entry["city"].lower()
            if city not in latest_entries:
                latest_entries[city] = entry

        cities = [entry["city"].title() for entry in latest_entries.values()]
        temps = [entry["temperature"] for entry in latest_entries.values()]

        if len(cities) < 2:
            print("Need at least two different cities for comparison.")
            return

        plt.figure()
        plt.bar(cities, temps)
        plt.title("Temperature Comparison Between Cities")
        plt.xlabel("City")
        plt.ylabel("Temperature (°C)")
        plt.tight_layout()
        plt.grid(True, axis='y')
        plt.show()
