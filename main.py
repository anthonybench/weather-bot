#!/usr/bin/env python
#╔═══════════════════════════════════
#║ SleepySoft | Private Server
#║ WeatherBot
#║
#║   ▶ Isaac Yep
#╚══════════════════════════════════
mainDocString = '''
This program logs in as a discord bot and responds to pre-defined weather data requests ('slash commands', or most often just 'commands').
Requires 
'''

#───Dependencies───────────────
# stdlib
from sys import argv, exit, getsizeof
from typing import List
from subprocess import run
from typing import Optional
import requests
import json
from datetime import datetime
# custom modules
from toolchain.option_utils import usageMessage, checkListOverlap, verifyOption, getOptionVal, stripOptionVals
from toolchain.slash_commands import currentLogic, forecastLogic, airQualityLogic
# 3rd party
try:
  from yaml import safe_load, YAMLError
  from discord import Client, Intents, File, app_commands, Object, Interaction
  import discord.ext
  # import features # TODO: implement
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)

#───Parameters─────────────────
userArgs = argv[1:]
minArgs  = 0
maxArgs  = 1
options  = { # ['--takes-arg=', 'int'|'str']
  'help' : ['-h', '--help'],
}
latitude     = 45.6280
longitude    = -122.6739

#───Entry──────────────────────
def main():
  ## Invalid number of args
  if len(userArgs) < (minArgs) or len(userArgs) > (maxArgs):
    usageMessage(f"Invalid number of options in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Invalid option
  if (len(userArgs) != 0) and not (verifyOption(userArgs, options)):
    usageMessage(f"Invalid option(s) entered in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Help option
  if checkListOverlap(userArgs, options['help']):
    print(mainDocString, end='')
    usageMessage()
    exit(0)
  else:
    with open('creds.yml', 'r') as raw_config:

      # load credentials
      config_dict   = safe_load(raw_config)
      app_id        = config_dict['app_id']
      public_key    = config_dict['public_key']
      perms_int     = config_dict['perms_int']
      token         = config_dict['token']
      client_id     = config_dict['client_id']
      client_secret = config_dict['client_secret']
      guild_id      = config_dict['guild_id']
      api_key       = config_dict['open_weather_key']

      # client class
      guild = discord.Object(id=guild_id)
      class MyClient(discord.Client):
        def __init__(self, *, intents: discord.Intents):
          super().__init__(intents=intents)
          self.tree = app_commands.CommandTree(self)

        async def setup_hook(self):
          self.tree.copy_global_to(guild=guild)
          await self.tree.sync(guild=guild)

      # init
      intents = Intents(messages=True, guilds=True, members=True)
      client  = MyClient(intents=intents)

      #═══Commands══════════════════════❗
      @client.event
      async def on_ready():
        """Log successful login"""
        print(f'Logged in as {client.user} (ID: {client.user.id})')
        print('──────')

      @client.tree.command()
      async def current(interaction: discord.Interaction):
        """Gets current weather conditions."""
        message = currentLogic(api_key, longitude, latitude)
        await interaction.response.send_message(message)

      @client.tree.command()
      async def forecast(interaction: discord.Interaction):
        """Gets seven day forecast."""
        message = forecastLogic(api_key, longitude, latitude)
        await interaction.response.send_message(message)

      @client.tree.command()
      async def airquality(interaction: discord.Interaction):
        """Gets current air quality metrics."""
        message = airQualityLogic(api_key, longitude, latitude)
        await interaction.response.send_message(message)
      #═════════════════════════════════❗

      # exec
      try:
        client.run(token)
      except Exception as e:
        print(f'Error on attempted login:\n{e}')

    exit(1)


#───Exec───────────────────────
if __name__ == "__main__":
    main()
