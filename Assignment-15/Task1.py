import requests
import json

def get_weather(city):
    # api_key = "d93dd9688a31dbe833fdcd9f2cc76bdb"
    api_key = "cac0fc82fb3e06f734c8d6e8db3284d8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    print(json.dumps(weather_data, indent=4))
    return weather_data

# Get city name from user
city_name = input("Enter city name: ")
get_weather(city_name)