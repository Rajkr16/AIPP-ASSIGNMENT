import requests
import json

API_KEY = "cac0fc82fb3e06f734c8d6e8db3284d8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
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

    # HTTP status handling
    if response.status_code == 401:
        print("Error: Unauthorized. Check the API key.")
        return None
    if response.status_code == 404:
        print("Error: City not found.")
        return None
    if response.status_code >= 500:
        print("Error: Weather service unavailable. Try again later.")
        return None
    if response.status_code != 200:
        print(f"Error: Unexpected status code {response.status_code}.")
        return None

    # Parse JSON safely
    try:
        weather_data = response.json()
    except ValueError:
        print("Error: Failed to decode response JSON.")
        return None

    # API-level error inside JSON (OpenWeather sometimes puts cod/message)
    cod = weather_data.get("cod")
    if cod != 200:
        print(f"Error: {weather_data.get('message', 'Unknown API error.')}")
        return None

    print(json.dumps(weather_data, indent=4))
    return weather_data

if __name__ == "__main__":
    city_name = input("Enter city name: ").strip()
    if city_name:
        get_weather(city_name)
    else:
        print("Error: City name cannot be empty.")