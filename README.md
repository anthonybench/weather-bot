# **WeatherBot**
*A Discord application to fetch OpenWeather data.*

<br />

## **Welcome to WeatherBot!**
A succinctly written discord application to satisfy in-chat weather reports and forecasts.

Clone it, supply credentials, run it!

<br />

### **Table of Contents** 📖
<hr>

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
# Discord
app_id: # developer console
public_key: # developer console
perms_int: # developer console
token: # developer console
client_id: # developer console
client_secret: # developer console
guild_id: # server settings in discord
#
channel_scope:
  - channel-name
  - other-channel-name


# OpenWeather
open_weather_key: # openweather console
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
  - [OpenWeather](https://openweathermap.org/api)

<br />

## **Contribute 🤝**
<hr>

If you think you have a cool weather data idea, submit a PR 🤓

<br />

## **Acknowledgements 💙**
<hr>

Thanks to Jean Choi, my partner, for being so supportive all the time.

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