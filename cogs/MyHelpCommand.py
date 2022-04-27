from nextcord.ext import commands


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return super().get_command_signature(command)
