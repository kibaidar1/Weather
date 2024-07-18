import httpx

GEOCODE_URL = 'https://geocoding-api.open-meteo.com/v1/search'
FORECAST_URL = 'https://api.open-meteo.com/v1/forecast'


async def get_geocode(name: str):
    """Функция получения геоданных по названию города"""

    async with httpx.AsyncClient() as client:
        params = {'name': name,
                  'language': 'ru',
                  'count': 1}
        response = await client.get(GEOCODE_URL, params=params)
        print('_____________________________',response.headers)
        data = response.json()
        try:
            result = data['results'][0]
            latitude = result['latitude']
            longitude = result['longitude']
            city_name = f"{result['name']} ({result['country']} - {result['admin1']})"
            return {'city_name': city_name, 'latitude': latitude, 'longitude': longitude}
        except Exception:
            return None


async def get_weather_by_geocode(latitude: float, longitude: float):
    """Функция получения прогноза погоды по геоданным (координатам)"""

    async with httpx.AsyncClient() as client:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m",
                        'apparent_temperature',
                        'wind_speed_10m',
                        'relative_humidity_2m',
                        ]
        }
        response = await client.get(FORECAST_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            return {**weather_data['current']}

    return None


async def get_weather_by_city_name(city_name: str):
    """Функиця получения прогноза погоды по названию города"""

    geo_code = await get_geocode(city_name)
    if geo_code:
        weather_data = await get_weather_by_geocode(latitude=geo_code['latitude'],
                                                    longitude=geo_code['longitude'])
        if weather_data:
            return {'city_name': geo_code['city_name'], **weather_data}

    return None


