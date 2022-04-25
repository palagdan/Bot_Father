import discord
import slash as slash
from discord.ext import commands, tasks
import os
import requests
import json
import random
from itertools import cycle

TOKEN = 'OTY3MTA5OTc3OTc2MjM4MDgx.YmLhWg.orW16i7bV9_-2kPQiu5BlIeRpSU'

client = commands.Bot(command_prefix='/')


@client.command(name="first_command")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


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
