import requests
from django.shortcuts import render

def get_weather(request):
    lat, lon = 52.2298, 21.0122
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)
    weather_data = response.json().get("current_weather", {})

    return render(request, "weather/weather.html", {"weather": weather_data})
