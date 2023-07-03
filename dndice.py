# WIP: Will feature the DNDice cog.
import discord, asyncio
from discord.ext import commands
from strings import enemy_list_img

# Initalizes bot config.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

# !!!CLASS BELOW IS WIP!!!
class DNDice(commands.Cog):
    '''
    This is part of the Dungeons and Dragons functionality of the Discord bot.
    '''
    def __init__(self, bot):
        # Initial set-up of the DNDice function.
        # At the start of the game, it is turn 0 and no enemies are listed.
        self.bot = bot
        self.turn_number = 0
        self.enemy_list = ''
    
    @commands.command
    async def turn_order(self, ctx, *args):
        # Directly affects self.enemy_list.
        self.enemy_list = [enemy.strip() for enemy in " ".join(args).split(",")]
        await ctx.send(f"The current turn order is: {', '.join(self.enemy_list)}.")
        await asyncio.sleep(5); await ctx.message.delete()
    
    @commands.command
    async def turn(self, ctx):
        # Increases self.turn_number by 1. Creates an embed from a template.
        self.turn_number += 1
        enemy_list = discord.Embed(
            title = f'Turn #{self.turn_number}',
            color = discord.Color.from_rgb(255, 255, 255))
        enemy_list.set_thumbnail(url = enemy_list_img)
        if self.enemy_list:
            # Checks if self.enemy_list is empty. If it is not, edits enemy_list() with their turn order.
            enemy_list.description = f'Turn Order: \n {", ".join(self.enemy_list)}'
        await ctx.send(embed = enemy_list)
        
    # TO-DO: add turn_end, initiative, support, campaign, roll


# !!!CLASS BELOW IS WIP!!!
class TimeConversion(commands.Cog):
    '''
    This is for the time conversion. Small thing that converts times from UTC in UK/DE time.
    '''
    ...

