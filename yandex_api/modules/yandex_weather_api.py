import requests
import json

from settings import KEY


def get_weather_by_lat_lon(lat, lon):
    headers = {
        'X-Yandex-API-Key': KEY,
    }

    params = (
        ('lat', lat),
        ('lon', lon),
        ('lang', 'ru_RU'),
    )

    response = requests.get('https://api.weather.yandex.ru/v1/informers', params=params, headers=headers)
    json_data = response.json()
    return json_data
