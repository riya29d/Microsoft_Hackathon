import requests
import datetime as dt

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "493fee0cf7c2b14937653f997b28d07f" # Replace with your OpenWeatherMap API key

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * (9/5) + 32
    return celsius, fahrenheit

city_name = input("Enter city name: ")

try:
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url).json()

    if response["cod"] == 200:
        temp_kel = response["main"]["temp"]
        temp_cel, temp_fah = kelvin_to_celsius_fahrenheit(temp_kel)
        feels_like_kel = response["main"]["feels_like"]
        feels_like_cel, feels_like_fah = kelvin_to_celsius_fahrenheit(feels_like_kel)
        humidity = response["main"]["humidity"]
        description = response["weather"][0]["description"]
        sunrise_time = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
        sunset_time = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])
        wind_speed = response["wind"]["speed"]

        print(f"Temperature in {city_name}: {temp_cel:.2f}°C/{temp_fah:.2f}°F")
        print(f"Temperature in {city_name} feels like: {feels_like_cel:.2f}°C/{feels_like_fah:.2f}°F")
        print(f"Humidity in {city_name}: {humidity}%")
        print(f"Wind speed in {city_name}: {wind_speed} m/s")
        print(f"General Weather in {city_name}: {description}")
        print(f"Sun rises in {city_name} at {sunrise_time} local time")
        print(f"Sun sets in {city_name} at {sunset_time} local time")
    else:
        print(f"Error: {response['message']}")
except requests.exceptions.RequestException as e:
    print("Error: Failed to connect to the weather service.")
except KeyError:
    print("Error: Failed to parse weather data.")
except Exception as e:
    print(f"Error: {str(e)}")
