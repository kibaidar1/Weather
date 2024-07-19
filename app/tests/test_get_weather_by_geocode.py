import pytest
from aioresponses import aioresponses

from app.utils.open_meteo import get_weather_by_geocode

TEST_DATA = {'latitude': 55.75222,
             'longitude': 37.61556,
             'success_response': {'current': {
                 'temperature_2m': 20,
                 'apparent_temperature': 19,
                 'wind_speed_10m': 5,
                 'relative_humidity_2m': 60}}
             }
# FORECAST_URL = (f"https://api.open-meteo.com/v1/forecast?latitude={TEST_DATA['latitude']}&"
#                 f"longitude={TEST_DATA['longitude']}$"
#                 f"current=temperature_2m$"
#                 f"current=apparent_temperature$"
#                 f"current=wind_speed_10m$"
#                 f"current=relative_humidity_2m")




# @pytest.mark.asyncio
# async def test_get_weather_by_geocode_success():
#
#
#     with aioresponses() as mocked:
#         mocked.get(FORECAST_URL,
#                    payload=TEST_DATA['success_response'])
#
#         result = await get_weather_by_geocode(TEST_DATA['latitude'],
#                                               TEST_DATA['longitude'])
#         print(result)
#
#         assert result == TEST_DATA['success_response']['current']




@pytest.mark.asyncio
async def test_get_weather_by_geocode_invalid():

    with aioresponses() as mocked:
        mocked.get('https://kek', status=400)

        result = await get_weather_by_geocode('latitude',
                                              'longitude')

        assert result is None
