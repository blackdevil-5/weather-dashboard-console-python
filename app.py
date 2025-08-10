#This is app.py which will be used for the users interaction
from weather_api import WeatherApi
from storage import WeatherStore
from visualize import WeatherVisual

class WeatherApp:
    def __init__(self):
        #We r initializing the classes from other modules
        self.api = WeatherApi()
        self.store = WeatherStore()
        self.visual = WeatherVisual()
    
    def display_menu(self):
        #Here we will display menu for the dashboard program
        print("--- Weather Tracker App ---")
        print("1. Fetch Current Weather")
        print("2. View Weather History")
        print("3. Search by City or Date")
        print("4. Plot Temperature Trend")
        print("5. Plot City Comparison")
        print("6. Exit")

    def ch_handler(self, choice):
        if choice == "1":
            city = input("Enter city name: ")
            weather = self.api.fetch_weather(city)
            if weather:
                self.store.save_data(weather)
                print(f"✅ Weather fetched and saved for {city.title()}")

        elif choice == "2":
            data = self.store.load_data()
            if not data:
                print("📂 No weather history found.")
            else:
                print("\n📜 Weather History:")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                for i, entry in enumerate(data, start=1):
                    print(f"📍 Entry #{i}")
                    print(f"🏙  City        : {entry.get('city', 'N/A').title()}")
                    print(f"🌡  Temperature: {entry.get('temperature', 'N/A')}°C")
                    print(f"💧  Humidity   : {entry.get('humidity', 'N/A')}%")
                    print(f"☁️  Condition  : {entry.get('condition', 'N/A')}")
                    print(f"🌬  Wind Speed : {entry.get('wind_speed', 'N/A')} km/h")
                    print(f"📅  Date       : {entry.get('date', 'N/A')}")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        elif choice == "3":
            key = input("Search by city or date: ").lower()
            results = self.store.search_data(key)
            if not results:
                print("No matching results found.")
            else:
                for entry in results:
                    print(entry)

        elif choice == "4":
            city = input("Enter city for temperature trend: ")
            self.visual.plot_temperature_trend(city)

        elif choice == "5":
            self.visual.plot_city_comparison()

        else:
            print("❌ Invalid input, try again.")

    def run(self):
        #this runs the main concept of the app.py
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '6':
                print("Thank You for visiting us, Bye...")
                break
            self.ch_handler(choice)

# Entry point to run the app
if __name__ == "__main__":
    app = WeatherApp()
    app.run()