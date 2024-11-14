import requests

api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def getCurrentWeatherData(lat, lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric").json()

    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']

    return [weather, temp]
