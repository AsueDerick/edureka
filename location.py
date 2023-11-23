import sys
import requests

def get_location_params(location):
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": location,
        "key": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "OK":
            result = data["results"][0]["geometry"]["location"]
            print(f"Latitude: {result['lat']}, Longitude: {result['lng']}")
        else:
            print(f"Error: {data['status']} - {data.get('error_message', '')}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python location.py <location_name>")
    else:
        location_name = sys.argv[1]
        get_location_params(location_name)
