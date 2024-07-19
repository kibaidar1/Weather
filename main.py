import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import open_meteo

app = FastAPI()
staticfiles = StaticFiles(directory='app/static')
app.mount("/static", staticfiles, name="static")
templates = Jinja2Templates(directory='app/templates')


@app.get("/", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = None):
    if city:
        weather_data = await open_meteo.get_weather_by_city_name(city)
        print(weather_data)
        return templates.TemplateResponse(name='index.html',
                                          context={'weather_data': weather_data,
                                                   'city': city,
                                                   'request': request})
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app='main:app')
