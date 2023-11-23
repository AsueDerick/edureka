import sys
import requests

def get_weather(api_key, city_id):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "id": city_id,
        "appid": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        main_data = data.get("main", {})
        wind_data = data.get("wind", {})
        cloud_data = data.get("clouds", {})
        sys_data = data.get("sys", {})

        print(f"Temperature: {main_data.get('temp')}K")
        print(f"Min Temperature: {main_data.get('temp_min')}K")
        print(f"Max Temperature: {main_data.get('temp_max')}K")
        print(f"Windspeed: {wind_data.get('speed')} m/s")
        print(f"Humidity: {main_data.get('humidity')}%")
        print(f"Cloudiness: {cloud_data.get('all')}%")
        print(f"Pressure: {main_data.get('pressure')} hPa")
        print(f"Sunrise: {sys_data.get('sunrise')}")
        print(f"Sunset: {sys_data.get('sunset')}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python weather.py <api_key> <city_id>")
    else:
        api_key = sys.argv[1]
        city_id = sys.argv[2]
        get_weather(api_key, city_id)
