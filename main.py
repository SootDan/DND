'''
This is the main file for the Discord bot.
It is required to start the bot; without any of the other
files, it will not have any functionality.
'''
import discord, asyncio
from discord.ext import commands
from privatefiles import token # Conceals token string for privacy

# Adds asyncio cogs
from dndice import DNDice, Support

# Initalizes bot config.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

# Cogs for the bot
dnd = DNDice(bot) # Makes class import into a module, e.g. dnd.turn_order()
support = Support(bot)

@bot.event
async def on_ready():
    # Called when bot finished initializing.
    activity = discord.Game(name = 'Prometheus', type = 3) # Displays a status
    await bot.change_presence(status = discord.Status.online, activity = activity)
    print(f'Logged on as {bot.user}! ID: {bot.user.id}') # Prints out to console

async def main():
    # Adds bot functionality.
    async with bot:
        # TO-DO: add music functionality, timeconversion
        await bot.add_cog(dnd) # DNDice module (dndice.py)
        await bot.add_cog(support) # Support module (dndice.py)
        await bot.start(token)

asyncio.run(main()) # Runs the bot! Should print out a log as defined by on_ready()