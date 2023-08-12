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
with open('config.yml', 'r') as raw_config:
  try:
    config = safe_load(raw_config)
  except YAMLError as e:
    print("Error. YAML input invalid.\n{e}")
    exit(1)
  app_id        = config['app_id']
  public_key    = config['public_key']
  perms_int     = config['perms_int']
  token         = config['token']
  client_id     = config['client_id']
  client_secret = config['client_secret']
  guild_id      = config['guild_id']
  api_key       = config['open_weather_key']
  channel_scope = config['channel_scope']
latitude  = 45.6280
longitude = -122.6739


#───Commands─────────────────
@app.command()
def run() -> None:
  '''Weather Bot

  Runs Discord bot that fetches climate data from the OpenWeather API upon slash-command chat dictation.
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

  @client.event
  async def on_ready():
    '''Print successful login'''
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('──────')


  ## Commands
  #───
  @client.tree.command()
  async def help(interaction:Interaction):
    '''Explain WeatherBot usage'''
    if interaction.channel.name in channel_scope:
      message = f'''/forecast :: *5 day forecast*
/current :: *current climate conditions*
/airquality :: *current air quality metrics*'''
      await interaction.response.send_message(message)
    else:
      message = f'Sorry, i only respond in {", ".join(channel_scope)}'
      await interaction.response.send_message(message, ephemeral=True)  
  #───
  @client.tree.command()
  async def current(interaction: discord.Interaction):
    '''Current weather conditions.'''
    if interaction.channel.name in channel_scope:
      message = current_logic(api_key, longitude, latitude)
      await interaction.response.send_message(message)
    else:
      message = f'Sorry, i only respond in {", ".join(channel_scope)}'
      await interaction.response.send_message(message, ephemeral=True)
  #───
  @client.tree.command()
  async def forecast(interaction: discord.Interaction):
    '''Seven day forecast.'''
    if interaction.channel.name in channel_scope:
      message = forecast_logic(api_key, longitude, latitude)
      await interaction.response.send_message(message)
    else:
      message = f'Sorry, i only respond in {", ".join(channel_scope)}'
      await interaction.response.send_message(message, ephemeral=True)
  #───
  @client.tree.command()
  async def airquality(interaction: discord.Interaction):
    '''Current air quality metrics'''
    if interaction.channel.name in channel_scope:
      message = air_quality_logic(api_key, longitude, latitude)
      await interaction.response.send_message(message)
    else:
      message = f'Sorry, i only respond in {", ".join(channel_scope)}'
      await interaction.response.send_message(message, ephemeral=True)
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
