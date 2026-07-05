import os
import asyncio
import discord
from discord.ext import commands

from config import TOKEN
from database.database import init_database

# ==============================
# Discord Intents
# ==============================

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
intents.messages = True

# ==============================
# Bot
# ==============================

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# ==============================
# Cog List
# ==============================

COGS = [
    "cogs.events",
    "cogs.whitelist",
    "cogs.antiscam",
    "cogs.settings",
    "cogs.moderation",
]

# ==============================
# Ready Event
# ==============================

@bot.event
async def on_ready():

    print("=" * 50)
    print(f"Logged in as : {bot.user}")
    print(f"Bot ID       : {bot.user.id}")
    print(f"Guilds       : {len(bot.guilds)}")
    print("=" * 50)

    try:
        synced = await bot.tree.sync()
        print(f"✓ Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# ==============================
# Load Extensions
# ==============================

async def load_extensions():

    for extension in COGS:

        try:
            await bot.load_extension(extension)
            print(f"✓ Loaded {extension}")

        except Exception as e:
            print(f"✗ Failed to load {extension}")
            print(e)

# ==============================
# Main
# ==============================

async def main():

    init_database()

    async with bot:

        await load_extensions()

        await bot.start(TOKEN)

# ==============================
# Start
# ==============================

if __name__ == "__main__":
    asyncio.run(main())