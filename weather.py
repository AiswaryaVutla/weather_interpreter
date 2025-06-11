import requests


def get_weather_data(location, api_key, unit='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': unit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
    return None


def display_weather(data, unit):
    if data:
        city = data.get('name')
        country = data['sys'].get('country')
        temp = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        condition = data['weather'][0].get('description').title()

        unit_symbol = '°C' if unit == 'metric' else '°F'

        print(f"\nWeather in {city}, {country}:")
        print(f"Condition : {condition}")
        print(f"Temperature: {temp}{unit_symbol}")
        print(f"Humidity  : {humidity}%")
    else:
        print("Unable to retrieve weather data.")


def main():
    api_key = "7570ccf8dbffe4eb0c66c851e97d7550"

    print("=== Weather App ===")
    location = input("Enter city or ZIP code: ").strip()

    while True:
        unit_input = input("Choose temperature unit (C for Celsius / F for Fahrenheit): ").strip().upper()
        if unit_input in ['C', 'F']:
            unit = 'metric' if unit_input == 'C' else 'imperial'
            break
        else:
            print("Invalid input. Please enter 'C' or 'F'.")

    weather_data = get_weather_data(location, api_key, unit)
    display_weather(weather_data, unit)


if __name__ == "__main__":
    main()