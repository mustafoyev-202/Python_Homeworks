import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

lat = 41.311081
lon = 69.240562
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()
print(data)

if response.status_code:
    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description}")
else:
    print("Failed to retrieve data")
