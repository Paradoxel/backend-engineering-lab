import requests

API_KEY = "bbb064bfb29743a7cdc258283a716cfb"

def fetch_weather(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    return response

def format_weather(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind": data["wind"]["speed"]
    }

def get_weather():
    city = input("Enter city name: ")

    response = fetch_weather(city)
    data = response.json()

    if response.status_code != 200:
        print("Error:", data.get("message"))
        return

    weather = format_weather(data)

    print("\n--- WEATHER INFO ---")
    print(weather)



get_weather()