'''
This is the main file for the Discord bot.
It is required to start the bot; without any of the other
files, it will not have any functionality.
'''
import discord, asyncio
from discord.ext import commands
from privatefiles import token # Conceals token string

# Initalizes bot config.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
async def on_ready():
    # Called when bot finished initializing.
    activity = discord.Game(name = 'Prometheus', type = 3) # Displays a status
    await bot.change_presence(status = discord.Status.online, activity = activity)
    print(f'Logged on as {bot.user}! ID: {bot.user.id}') # Prints out to console

async def main():
    # Adds bot functionality.
    async with bot:
        # TO-DO: add music functionality, timeconversion, dice
        await bot.start(token)

asyncio.run(main()) # Runs the bot! Should print out a log as defined by on_ready()