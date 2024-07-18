from pydantic import BaseModel
from datetime import datetime


class WeatherResponse(BaseModel):
    city: str
    temperature: int
    apparent_temperature: int
    wind_speed: float
    relative_humidity: int
    rain: float
    snowfall: float


class SearchHistory(BaseModel):
    city: str
    timestamp: datetime

    class Config:
        orm_mode = True