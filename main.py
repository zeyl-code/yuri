import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="y!", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user, bot.user.id)

    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()