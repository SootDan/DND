'''
This is the main file for the Discord bot.
It is required to start the bot; without any of the other
files, it will not have any functionality.
'''
import discord, asyncio
from discord.ext import commands
from Assets.privatefiles import token # Conceals token string for privacy

# Adds asyncio cogs
from Modules.dndice import DNDice, Support, TimeConversion
from Modules.voice import Voice

# Initalizes bot config.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

# Sets up in-depth logging for debugging. Comment away if only running the bot.
# discord.utils.setup_logging()

# Cogs for the bot
dnd = DNDice(bot) # Makes class import into a module, e.g. dnd.turn_order()
support = Support(bot)
timeconversion = TimeConversion(bot)
voice = Voice(bot) # Still WIP, soundboard works. 

@bot.event
async def on_ready():
    # Called when bot finished initializing.
    activity = discord.Game(name = 'Prometheus', type = 3) # Displays a status
    await bot.change_presence(status = discord.Status.online, activity = activity)
    print(f'Logged on as {bot.user}! ID: {bot.user.id}') # Prints out to console


async def main():
    # Adds bot functionality.
    async with bot:
        await bot.add_cog(dnd) # dndice.py
        await bot.add_cog(support) # dndice.py
        await bot.add_cog(timeconversion) # dndice.py
        await bot.add_cog(voice) # voice.py | Only soundboard works, YT integration WIP
        await bot.start(token)

asyncio.run(main()) # Runs the bot! Should print out a log as defined by on_ready()
