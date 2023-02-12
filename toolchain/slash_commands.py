import requests
from datetime import datetime


def currentLogic(api_key: str, longitude: float, latitude: float) -> str:
    """takes open-weather api key and coordinates, fetches current weather data from open-weather, returns formatted message"""
    call = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    r = requests.get(call)
    j = r.json()
    weather_description = j['weather'][0]['description']
    date                = datetime.now()
    temp                = round(j['main']['temp'] - 273.15, 1) # degC
    high                = round(j['main']['temp_max'] - 273.15, 1) # degC
    low                 = round(j['main']['temp_min'] - 273.15, 1) # degC
    wind_speed          = j['wind']['speed'] # m/s
    humidity            = j['main']['humidity'] # %
    return f'''**Summary**: "{weather_description}" │ *{date.strftime("%-d %B %Y")}*\n
**🌡️ Temp**: `{temp} °C`"
   ☝ High: `{high} °C`
   👇 Low: `{low} °C`\n
**🌬️ Wind**: `{wind_speed} m/s`
**💧 Humidity**: `{humidity} %`
'''


def forecastLogic(api_key: str, longitude: float, latitude: float) -> str:
    """takes open-weather api key and coordinates,fetches 5-day 3-hour forecast data from open-weather, returns formatted message"""
    call = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}'
    r = requests.get(call)
    j = r.json()
    # return f''''''
    pass


def airquality() -> str:
  """TODO"""
  # https://openweathermap.org/api/air-pollution
  pass