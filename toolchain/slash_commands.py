import requests
from datetime import datetime
from statistics import mode, mean


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
    return f'''**{date.strftime("%A, %B %-d")}**\n"*{weather_description}*"\n> 🌡️ Temp: `{temp} °C`"\n>   ☝ High: `{high} °C`\n>   👇 Low: `{low} °C`\n> 🌬️ Wind: `{wind_speed} m/s`\n> 💧 Humidity: `{humidity} %`
'''


def forecastLogic(api_key: str, longitude: float, latitude: float) -> str:
  """takes open-weather api key and coordinates,fetches 5-day 3-hour forecast data from open-weather, returns formatted message"""
  call = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}'
  r = requests.get(call)
  j = r.json()
  # {
  #   'unix_timestamp' : [
  #     description, high(degK), low(degK), wind_speed(m/s), humidity(%)
  #   ]
  # }
  filtered_data = { datetime.fromtimestamp(i['dt']) : [i['weather'][0]['description'], i['main']['temp_max'], i['main']['temp_min'], i['wind']['speed'], i['main']['humidity']] for i in j['list'] if datetime.now().strftime('%A') != datetime.fromtimestamp(i['dt']).strftime('%A') }
  # {
  #   'day_name' : [
  #     [descriptions], [highs(degC)], [lows(degC)], [wind_speed(m/s)], [average_humidity(%)]
  #   ]
  # } # 
  grouped_data = {}
  for i in list(set([i.strftime('%A') for i in filtered_data])):
    grouped_data[i] = [
      [filtered_data[rec][0] for rec in filtered_data if rec.strftime('%A') == i],
      [round(filtered_data[rec][1] - 273.15,1) for rec in filtered_data if rec.strftime('%A') == i],
      [round(filtered_data[rec][2] - 273.15,1) for rec in filtered_data if rec.strftime('%A') == i],
      [filtered_data[rec][3] for rec in filtered_data if rec.strftime('%A') == i],
      [filtered_data[rec][4] for rec in filtered_data if rec.strftime('%A') == i],
    ]
  # {
  #   'day_name' : [
  #     description_mode, average_high(degC), average_low(degC), average_wind_speed(m/s), average_humidity(%)
  #   ]
  # }
  transformed_data = { k : [mode(v[0]), round(mean(v[1]),1), round(mean(v[2]),1), round(mean(v[3]),1), round(mean(v[4]),1)] for k,v in grouped_data.items() }
  message = ''
  for k,v in transformed_data.items():
    message += f'**{k}**\n"*{v[0]}*"\n> ☝ Average High: `{v[1]} °C`\n> 👇 Average Low: `{v[2]} °C`\n> 🌬️ Average Wind: `{v[3]} m/s`\n> 💧 Average Humidity: `{v[4]} %`\n\n'
  return message


def airQualityLogic(api_key: str, longitude: float, latitude: float) -> str:
  """takes open-weather api key and coordinates,fetches air quality data from open-weather, returns formatted message"""
  call = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}'
  r = requests.get(call)
  j = r.json()
  aqi_text = [None, 'Good', 'Fair', 'Moderate', 'Poor', 'Very Poor']
  particulate_labels = {'co':'CO', 'nh3':'NH3', 'no2':'NO2', 'o3':'O3', 'pm10':'Course Particulates', 'pm2_5':'Fine Particulates', 'so2':'SO2', 'no':'NO'}
  particulates = { particulate_labels[k] : v for k,v in j['list'][0]['components'].items()}
  aqi = j['list'][0]['main']['aqi']
  message = f'**{datetime.now().strftime("%A, %B %-d")}**\nAir Quality Index: `{aqi} ({aqi_text[aqi]})`\n'
  for k,v in particulates.items():
    message += f'> {k}: `{v}`\n'
  return message