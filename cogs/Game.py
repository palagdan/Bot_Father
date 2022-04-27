import discord
import random

from discord.ext import commands


class Game(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="Ping")
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass in all arguments!")

    @commands.command(description='Choose Rock or Paper or Scissors')
    async def Rock_Paper_Scissors(self, ctx, choice):
        variants = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(variants)
        output = None
        if computer_choice == choice.lower():
            output = f"{computer_choice.upper()}\nIt's a draw buddy\nOne's more?"
        else:
            if (computer_choice == 'rock' and choice.lower() == 'scissors') or (
                    computer_choice == 'paper' and choice.lower() == 'rock') or (
                    computer_choice == 'scissors' and choice.lower() == 'paper'):
                output = f"{computer_choice.upper()}\nYou loose :(\nOne's more?:)"
            else:
                output = f"{computer_choice.upper()}\nYou win :(\nOne's more?:)"
        embed = discord.Embed(
            description=output,
            colour=discord.Colour.random()
        )
        embed.set_image(url='https://cdn.dribbble.com/users/976907/screenshots/4879640/dribbble_13.gif')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Game(client))
