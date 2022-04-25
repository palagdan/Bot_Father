import discord
import opensea
from discord.ext import commands


class Tools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description='Delete messages')
    async def clear(self, ctx, amount=1):
        if amount > 10:
            await ctx.send('Too much messages you want to delete')
        else:
            await ctx.channel.purge(limit=amount)

    @commands.command(description='Ban user')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} is kicked\nReason: {reason}')

    @commands.command(description='Ban user')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unban(self, ctx, *, member):
        banned_members = await ctx.guild.bans()
        first, second = member.split('#')

        for ban_entry in banned_members:
            user = ban_entry.user

            if (user.name, user.discriminator) == (first, second):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command(description='About')
    async def about(self, ctx):
        embed = discord.Embed(
            title='About',
            description='This is the nft-bot, that allows you to retrieve information about collections, assets, '
                        'art etc',
            colour=discord.Colour.blue(),

        )
        embed.set_footer(text='Author: Daniil Palagin')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Tools(client))
