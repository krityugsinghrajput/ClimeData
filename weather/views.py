import requests
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WeatherSearch
from .serializers import WeatherSearchSerializer

def get_coordinates(city):
    """Convert city name to latitude and longitude using OpenStreetMap API."""
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
    headers = {"User-Agent": "ClimeData/1.0 (your@email.com)"}  # Replace with your email

    response = requests.get(url, headers=headers)  # Add headers
    try:
        response_json = response.json()
        if response_json:
            return response_json[0]['lat'], response_json[0]['lon']
        return None, None
    except requests.exceptions.JSONDecodeError:
        return None, None


@api_view(['GET'])
def get_weather(request, city):
    """Fetch weather data from Open-Meteo using latitude & longitude."""

    # Check if data is cached (less than 10 min old)
    cached_weather = WeatherSearch.objects.filter(city=city).first()
    if cached_weather and (now() - cached_weather.created_at).seconds < 600:
        serializer = WeatherSearchSerializer(cached_weather)
        return Response(serializer.data)

    # Convert city to latitude & longitude
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return Response({"error": "City not found"}, status=404)

    # Fetch weather data from Open-Meteo
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()

        # Save to database (caching)
        weather_entry, created = WeatherSearch.objects.update_or_create(
            city=city, defaults={'data': weather_data, 'created_at': now()}
        )
        return Response(weather_data)
    else:
        return Response({"error": "Weather data not found"}, status=500)
