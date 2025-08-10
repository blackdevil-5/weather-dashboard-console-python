#This module is used to store the data from the weather report
import json
import os

class WeatherStore:
    def __init__(self, filename="weather_data.json"):
        self.filename = filename

    def save_data(self, new_entry):
        try:
            data = self.load_data()
            data.append(new_entry)
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
            print("✅ Weather data saved.")
        except Exception as e:
            print("❌ Error saving data:", e)

    def load_data(self):    
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except Exception as e:
            print("❌ Error loading data:", e)
            return []
        
    def search_data(self, city=None, date=None):
        results = []
        data = self.load_data()
        for entry in data:
            if city and city.lower() not in entry['city'].lower():
                continue
            if date and date not in entry['date']:
                continue
            results.append(entry)
        return results