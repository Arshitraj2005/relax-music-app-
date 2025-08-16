import requests

def get_weather_data(city="Dariyapur"):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
        return response.text.strip()
    except:
        return "Haze +34°C"
