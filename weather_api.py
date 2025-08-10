#This module is used to fetch the data through API and present the information
import requests
from datetime import datetime as dt

class WeatherApi:
    def __init__(self):
        self.api_base_url = "https://wttr.in"

    def fetch_weather(self, city):
        try:
            url = f"{self.api_base_url}/{city}?format=j1"
            response = requests.get(url)

             # Connection failed or status not 200
            if response.status_code != 200:
                print(f"⚠️ Unable to reach weather API. Status code: {response.status_code}")
                return None
            
            data =  response.json()

            # Sanity check: expected data should be present
            if "current_condition" not in data or not data["current_condition"]:
                print("⚠️ API responded but no weather data found for this city.")
                return None
            
            current = data["current_condition"][0]

            weather_data = {
                "city": city.title(),
                "date": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": float(current["temp_C"]),
                "humidity": int(current["humidity"]),
                "condition": current["weatherDesc"][0]["value"],
                "wind_speed": float(current["windspeedKmph"])
            }

            return weather_data

        except Exception as e:
            print("⚠️ Error fetching weather data:", e)
            return None