# weather-dashboard-console-python
Simple Python console application to fetch and display weather data using API calls.
 🌤 Weather Monitoring Dashboard

 📌 Overview
The Weather Monitoring Dashboard is a Python-based application that allows users to fetch, store, search, and visualize weather data for different cities. It uses the wttr.in API (no API key required) to retrieve real-time weather details.

This project is designed using OOP concepts for better modularity and maintainability.

---

 📦 Features

 Core Functions
- Input a city name and fetch its current weather data
- Displays:
  - Temperature (°C)
  - Humidity (%)
  - Weather condition (Clear, Cloudy, Rainy, etc.)
  - Wind speed (km/h)

 Data Management
- Save all fetched data to a local file (`weather_data.json`)
- View history of weather queries
- Search weather history by city name or date
- Prevents visualization unless sufficient data is available

 Visualization
- Temperature Trend Line Graph for a single city over multiple days
- Bar Chart Comparison of multiple cities on the same date
- Implemented using `matplotlib`

 Error Handling
- Handles no internet connection
- Handles API downtime and empty responses
- Provides user-friendly error messages

---

 ⚙️ Requirements
- Python 3.8+
- `requests`
- `matplotlib`

Install dependencies:
```bash
pip install requests matplotlib
