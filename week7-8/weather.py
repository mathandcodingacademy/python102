# weather.py — Reference Implementation
# Week 7: AI Weather Mood App
#
# This is the reference — try building your own version with AI first (see README.md).
# If you're comparing: read your AI's version line by line against this one.

import requests
from config import API_KEY

# ============================================================
# CONFIGURATION
# API_KEY comes from config.py, NOT from this file. config.py is gitignored
# so your real key never gets committed. If config.py doesn't exist yet,
# copy config_example.py, rename the copy to config.py, and put your real
# key in there. Get a free key at: https://openweathermap.org/ → API Keys
# New keys can take up to 2 hours to activate (usually 10-20 min).
# Test your key with curl BEFORE running this file — see week7-8/README.md step 2.
# ============================================================
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Mood mapping: OpenWeatherMap condition → our mood word
# Full list of conditions: https://openweathermap.org/weather-conditions
MOOD_MAP = {
    "Clear":        "sunny",
    "Clouds":       "cloudy",
    "Rain":         "rainy",
    "Drizzle":      "rainy",
    "Thunderstorm": "stormy",
    "Snow":         "snowy",
    "Mist":         "foggy",
    "Smoke":        "foggy",
    "Haze":         "foggy",
    "Dust":         "foggy",
    "Fog":          "foggy",
    "Sand":         "foggy",
    "Ash":          "foggy",
    "Squall":       "stormy",
    "Tornado":      "stormy",
}


def get_weather(city):
    """
    Fetch current weather for a city from OpenWeatherMap.

    Parameters:
        city (str): City name, e.g. "London" or "Tokyo"

    Returns:
        dict with keys:
            city        (str)   — city name as returned by the API
            country     (str)   — two-letter country code, e.g. "GB"
            temp        (float) — temperature in Celsius
            feels_like  (float) — feels-like temperature in Celsius
            humidity    (int)   — humidity percentage
            condition   (str)   — main condition, e.g. "Rain", "Clear"
            description (str)   — detailed description, e.g. "light rain"
            wind_speed  (float) — wind speed in metres per second

    Raises:
        ValueError   — if the city name is not found (HTTP 404)
        RuntimeError — for any other non-200 HTTP response
    """
    params = {
        "q":     city,
        "appid": API_KEY,
        "units": "metric",   # Celsius; use "imperial" for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)

    # Why check status_code before calling .json()?
    # A 404 response still has a JSON body — but it's an error body, not weather data.
    # Checking first lets us give a clear error message instead of a confusing KeyError.
    if response.status_code == 404:
        raise ValueError(f"City '{city}' not found. Check the spelling and try again.")
    if response.status_code == 401:
        raise RuntimeError("Invalid API key. Check your API_KEY in weather.py.")
    if response.status_code != 200:
        raise RuntimeError(f"Unexpected API response: HTTP {response.status_code}")

    data = response.json()

    # The API returns nested JSON. We flatten it into a clean, simple dict
    # so the rest of our program doesn't need to know about the nesting.
    return {
        "city":        data["name"],
        "country":     data["sys"]["country"],
        "temp":        round(data["main"]["temp"], 1),
        "feels_like":  round(data["main"]["feels_like"], 1),
        "humidity":    data["main"]["humidity"],
        "condition":   data["weather"][0]["main"],
        "description": data["weather"][0]["description"].capitalize(),
        "wind_speed":  data["wind"]["speed"],
    }


def get_mood(condition):
    """
    Map an OpenWeatherMap condition string to a mood word.

    Parameters:
        condition (str): e.g. "Rain", "Clear", "Thunderstorm"

    Returns:
        str: one of "sunny", "cloudy", "rainy", "stormy", "snowy", "foggy", "unknown"
    """
    return MOOD_MAP.get(condition, "unknown")


# ============================================================
# Quick test — run this file directly to check your API key works
# ============================================================
if __name__ == "__main__":
    city = input("Enter a city (e.g. Toronto or Paris,FR): ").strip()
    try:
        weather = get_weather(city)
        mood = get_mood(weather["condition"])
        print(f"\nCity:        {weather['city']}, {weather['country']}")
        print(f"Temperature: {weather['temp']}°C (feels like {weather['feels_like']}°C)")
        print(f"Condition:   {weather['condition']} — {weather['description']}")
        print(f"Humidity:    {weather['humidity']}%")
        print(f"Wind:        {weather['wind_speed']} m/s")
        print(f"Mood:        {mood}")
    except ValueError as e:
        print(f"City error: {e}")
    except RuntimeError as e:
        print(f"API error: {e}")
