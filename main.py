#!/usr/bin/env python

'''README
This program logs in as a discord bot and responds to defined weather data requests ('slash commands', or most often just 'commands').

Usage:
  ./main.py run

References:
  https://typer.tiangolo.com/
  https://discordpy.readthedocs.io/en/stable/api.html
'''

# stdlib
from sys import exit
# custom modules
from toolchain.commands import current_logic, forecast_logic, air_quality_logic
# 3rd party
try:
  import typer
  from yaml import safe_load, YAMLError
  from discord import Client, Intents, File, app_commands, Object, Interaction
  import discord.ext
except ModuleNotFoundError as e:
  print("Error. Missing one or more 3rd-party packages (pip install).")
  exit(1)


#───Globals──────────────────
app = typer.Typer()
with open('creds.yml', 'r') as raw_config:
  try:
    config_dict   = safe_load(raw_config)
  except YAMLError as e:
    print("Error. YAML input invalid.\n{e}")
    exit(1)
  app_id        = config_dict['app_id']
  public_key    = config_dict['public_key']
  perms_int     = config_dict['perms_int']
  token         = config_dict['token']
  client_id     = config_dict['client_id']
  client_secret = config_dict['client_secret']
  guild_id      = config_dict['guild_id']
  api_key       = config_dict['open_weather_key']
latitude  = 45.6280
longitude = -122.6739


#───Commands─────────────────
@app.command()
def run() -> None:
  '''Weather Bot

  Runs Discord bot that fetches climate data from the OpenWeather API upon slash-command chat dictation.

  ───Return\n
  None
  '''
  ## Init
  guild = discord.Object(id=guild_id)
  class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
      super().__init__(intents=intents)
      self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
      self.tree.copy_global_to(guild=guild)
      await self.tree.sync(guild=guild)
  intents = Intents(messages=True, guilds=True, members=True)
  client  = MyClient(intents=intents)


  ## Commands
  @client.event
  async def on_ready():
    '''Print successful login'''
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('──────')
  #───
  @client.tree.command()
  async def current(interaction: discord.Interaction):
    '''Current weather conditions.'''
    message = current_logic(api_key, longitude, latitude)
    await interaction.response.send_message(message)
  #───
  @client.tree.command()
  async def forecast(interaction: discord.Interaction):
    '''Seven day forecast.'''
    message = forecast_logic(api_key, longitude, latitude)
    await interaction.response.send_message(message)
  #───
  @client.tree.command()
  async def airquality(interaction: discord.Interaction):
    '''Current air quality metrics'''
    message = air_quality_logic(api_key, longitude, latitude)
    await interaction.response.send_message(message)
  #───


  ## Login
  try:
    client.run(token)
  except Exception as e:
    print(f'Error on attempted login:\n{e}')
  return None


#───Entry────────────────────
if __name__ == "__main__":
  app()
