# Day 21: Weather App using API

import requests

API_KEY = "your_api_key_here"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found!")
            return

        name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print(f"\nCity: {name}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather}")

    except Exception as e:
        print("Error:", e)


# Input
city = input("Enter city name: ")
get_weather(city)
