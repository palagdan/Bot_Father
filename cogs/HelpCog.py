from nextcord.ext import commands

from cogs.MyHelpCommand import MyHelpCommand


class HelpCog(commands.Cog, name="Help"):

    def __init__(self, client):
        self._original_help_command = client.help_command
        client.help_command = MyHelpCommand()
        client.help_command.cog = self

    def cog_unload(self):
        self.client.help_command = self._original_help_command


def setup(client):
    client.add_cog(HelpCog(client))
