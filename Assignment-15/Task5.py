import requests
import json
from datetime import datetime

API_KEY = "cac0fc82fb3e06f734c8d6e8db3284d8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=8)
    except requests.exceptions.InvalidURL:
        print("Error: The weather service URL is invalid.")
        return None
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Network problem. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An unexpected request error occurred: {e}")
        return None

    if response.status_code == 401:
        print("Error: Unauthorized. Check the API key.")
        return None
    if response.status_code == 404:
        print("Error: City not found. Please enter a valid city.")
        return None
    if response.status_code >= 500:
        print("Error: Weather service unavailable. Try again later.")
        return None
    if response.status_code != 200:
        print(f"Error: Unexpected status code {response.status_code}.")
        return None

    try:
        weather_data = response.json()
    except ValueError:
        print("Error: Failed to decode response JSON.")
        return None

    if str(weather_data.get("cod")) != "200":
        if weather_data.get("message", "").lower() == "city not found":
            print("Error: City not found. Please enter a valid city.")
        else:
            print(f"Error: {weather_data.get('message', 'Unknown API error.')}")
        return None

    name = weather_data.get("name", city)
    main = weather_data.get("main", {})
    temp = main.get("temp")
    humidity = main.get("humidity")
    weather_list = weather_data.get("weather", [])
    description = (weather_list[0].get("description") if weather_list else None)

    if temp is None or humidity is None or description is None:
        print("Error: Missing expected weather fields.")
        return None

    description = description.capitalize()
    
    result = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": name,
        "temperature_c": temp,
        "humidity_percent": humidity,
        "description": description
    }
    
    # Display as JSON
    print(json.dumps(result, indent=2))
    
    # Append to file
    try:
        with open("weather_log.txt", "a", encoding="utf-8") as f:
            f.write(json.dumps(result) + "\n")
        print("\nWeather data saved to weather_log.txt")
    except IOError as e:
        print(f"Error: Failed to save to file: {e}")
    
    return result

def show_weather():
    city = input("Enter city name: ").strip()
    if not city:
        print("Error: City name cannot be empty.")
        return
    get_weather(city)

if __name__ == "__main__":
    show_weather()