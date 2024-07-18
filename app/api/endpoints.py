from fastapi import HTTPException
from fastapi_cli.cli import app
from starlette.staticfiles import StaticFiles

from app.api import schemas
from app.utils import open_meteo


@app.get("/weather/{city}", response_model=schemas.WeatherResponse)
async def get_weather(city: str):
    weather_data = await open_meteo.get_weather_by_city_name(city)
    if weather_data is None:
        raise HTTPException(status_code=404, detail="City not found")
    return weather_data

# @app.get("/history", response_model=List[schemas.SearchHistory])
# def get_search_history(db: Session = Depends(database.get_db)):
#     return crud.get_search_history(db)

# Подключение фронтенда
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
