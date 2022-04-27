import discord
import slash as slash
from discord.ext import commands, tasks
import os
import requests
import json
import random
from itertools import cycle

from cogs.HelpCog import HelpCog

TOKEN = 'OTY3MTA5OTc3OTc2MjM4MDgx.YmLhWg.-yrig0ceFXm760pc--q1zq5k-2k'

# --------------------Custom class for command help---------------------------#
# class CustomHelper(commands.HelpCommand):
#     def __int__(self):
#         super().__init__()
#
#     async def send_bot_help(self, mapping):
#         for cog in mapping:
#             await self.get_destination().send(f'{cog.qualified_name()}: {[command.name for command in mapping[cog]]}')
#
# async def send_cog_help(self, cog): return self.get_destination().send(f'{cog.qualified_name}: {[command.name for
# command in cog.get_commands()]}')
#
#     async def send_group_help(self, group):
#         return self.get_destination().send(
#             f'{group.qualified_name}: {[command.name for index, command in enumerate(group.commands)]}')
#
#     async def send_command_help(self, command):
#         await self.get_destination().send(command.name)


client = commands.Bot(command_prefix='/')
# ------------------load new cog---------------------#
# @client.command(name="first_command")
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')

# ------------------unload cog---------------------#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    change_status.start()
    print(f'Bot ready')


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('/help'))


client.run(TOKEN)
