import discord
from discord.ext import commands

from utils.helpers import should_ignore_message


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("✓ Events Cog Loaded")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        # Ignore DMs
        if message.guild is None:
            return

        # Ignore bots, whitelisted users/channels
        if should_ignore_message(message):
            return

        # Ignore messages without content or attachments
        if not message.content and not message.attachments:
            return

        # Send message to AntiScam scanner
        antiscam = self.bot.get_cog("AntiScam")

        if antiscam:
            await antiscam.scan_message(message)


async def setup(bot):
    await bot.add_cog(Events(bot))