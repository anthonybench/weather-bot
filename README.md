# **WeatherBot**
*A Discord application to fetch OpenWeather data.*

<br />

## **Welcome to WeatherBot!**
A succinctly written discord application to satisfy in-chat weather reports and forecasts.

Clone it, supply credentials, run it!

<br />

### **Table of Contents** 📖
<hr>

  - [Welcome](#welcome-to-REPO)
  - [**Get Started**](#get-started-)
  - [Usage](#usage-)
  - [Technologies](#technologies-)
  - [Contribute](#Contribute-)
  - [Acknowledgements](#acknowledgements-)
  - [License/Stats/Author](#license-stats-author-)

<br />

## **Get Started 🚀**
<hr>

Fetch dependencies:
```sh
pip install -r requirements.txt
```

Create `creds.yml`  in the repo's root, and populate as follows:
```yaml
app_id: # dev console
public_key: # dev console
perms_int: # dev console
token: # dev console
client_id: # dev console
client_secret: # dev console
guild_id: # right click server in discord
open_weather_key: # open-weather api key
```

You can ensure your bot token is active or generate a new one [here](https://discord.com/developers/applications/1071317419039141929/bot).

See the [Discord.py API docs](https://discordpy.readthedocs.io/en/stable/api.html) to implement new features.

<br />

## **Usage ⚙**
<hr>

Run indefinitely:
```sh
./main.py
```

Info message:
```sh
./main.py --help
```

Chat commands (presuming you name your application `WeatherBot`):
```sh
# get current climate conditions
/WeatherBot current

# get 5-day climate forecast
/WeatherBot forecast

# get current air quality metrics
/WeatherBot airquality
```

<br />

## **Technologies 🧰**
<hr>

  - [Discord.py](https://google.com)
  - [PyYaml](https://google.com)
  - [Typer](https://typer.tiangolo.com/)

<br />

## **Contribute 🤝**
<hr>

If you think you have a cool weather data idea, submit a PR 🤓

<br />

## **Acknowledgements 💙**
<hr>

Great references:
- [Discord.py](https://google.com)
- [Bot Examples](https://github.com/Rapptz/discord.py/tree/v2.1.1/examples)
- [OpenWeather Endpoints, grouped by price](https://openweathermap.org/price#weather)
- [OpenWeather Keys](https://home.openweathermap.org/api_keys)

<br />

## **License, Stats, Author 📜**
<hr>

<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />

<!-- badge cluster -->
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/anthonybench/weather-bot) ![PyPI](https://img.shields.io/pypi/v/discord.py) ![GitHub top language](https://img.shields.io/github/languages/top/anthonybench/weather-bot)
<!-- / -->

See [License](LICENSE) for the full license text.

This repository was authored by *Isaac Yep*.

[Back to Table of Contents](#table-of-contents-)