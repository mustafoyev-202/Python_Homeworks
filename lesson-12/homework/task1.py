from bs4 import BeautifulSoup

with open("lesson-12/homework/weather.html", "r", encoding="utf-8") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

# Extract weather forecast details
forecast = []
rows = soup.find_all("tr")[1:]  # Skip the header row
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temperature = int(cols[1].text.replace("°C", "").strip())
    condition = cols[2].text.strip()
    forecast.append({"day": day, "temperature": temperature, "condition": condition})

# Display weather data
for entry in forecast:
    print(
        f"Day: {entry['day']}, Temperature: {entry['temperature']}°C, Condition: {entry['condition']}"
    )

# Find specific data
highest_temp = max(forecast, key=lambda x: x["temperature"])
sunny_days = [entry["day"] for entry in forecast if entry["condition"] == "Sunny"]

print(
    f"Day with the highest temperature: {highest_temp['day']} ({highest_temp['temperature']}°C)"
)
print(f"Days with 'Sunny' condition: {', '.join(sunny_days)}")

# Calculate average temperature
average_temp = sum(entry["temperature"] for entry in forecast) / len(forecast)
print(f"Average temperature for the week: {average_temp:.2f}°C")
