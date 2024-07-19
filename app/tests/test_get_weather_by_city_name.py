from unittest.mock import patch, AsyncMock

import pytest

from app.utils.open_meteo import get_weather_by_city_name


@pytest.mark.asyncio
async def test_get_weather_by_city_name_success():
    city_name = "Москва"
    geo_code = {
        'city_name': 'Москва (Россия - Москва)',
        'latitude': 55.7558,
        'longitude': 37.6176
    }
    weather_data = {
        "temperature_2m": 20,
        "apparent_temperature": 19,
        "wind_speed_10m": 5,
        "relative_humidity_2m": 60
    }

    expected_result = {
        'city_name': 'Москва (Россия - Москва)',
        "temperature_2m": 20,
        "apparent_temperature": 19,
        "wind_speed_10m": 5,
        "relative_humidity_2m": 60
    }

    with patch('app.utils.open_meteo.get_geocode', new=AsyncMock(return_value=geo_code)) as mock_get_geocode, \
            patch('app.utils.open_meteo.get_weather_by_geocode',
                  new=AsyncMock(return_value=weather_data)) as mock_get_weather_by_geocode:
        result = await get_weather_by_city_name(city_name)

        assert result == expected_result
        mock_get_geocode.assert_awaited_once_with(city_name)
        mock_get_weather_by_geocode.assert_awaited_once_with(latitude=geo_code['latitude'],
                                                             longitude=geo_code['longitude'])
