from aioresponses import aioresponses
import pytest
from app.utils.open_meteo import get_geocode


TEST_DATA = {'city_name': 'Москва',
             'city_geocode': {'city_name': 'Москва (Россия - Москва)', 'latitude': 55.75222, 'longitude': 37.61556},
             'success_response': {"results": [
                 {'name': 'Москва',
                  "country": 'Россия',
                  'admin1': 'Москва',
                  'latitude': 55.75222,
                  'longitude': 37.61556}]},
             'unknown_city': 'Неизвестный город',
             'not_found_response': {
                 'generationtime_ms': 0.77593327}
             }
GEOCODE_URL = 'https://geocoding-api.open-meteo.com/v1/search'


@pytest.mark.asyncio
async def test_get_geocode_success():

    with aioresponses() as mocked:
        mocked.get(GEOCODE_URL, payload=TEST_DATA['success_response'])

        result = await get_geocode(TEST_DATA['city_name'])

        assert result == TEST_DATA['city_geocode']


@pytest.mark.asyncio
async def test_get_geocode_not_found():

    with aioresponses() as mocked:
        mocked.get(GEOCODE_URL, payload=TEST_DATA['not_found_response'])

        result = await get_geocode(TEST_DATA['unknown_city'])

        assert result is None
