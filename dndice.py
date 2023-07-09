import discord, asyncio
from discord.ext import commands
from strings import img_enemy_list, desc_support, img_support, desc_campaign, img_campaign
from privatefiles import doc_campaign, char_baughl, char_erhice, char_morgan, char_orange, char_tootle, char_ylvie

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
    
    @commands.command()
    async def turn_order(self, ctx, *args):
        # Directly affects self.enemy_list.
        self.enemy_list = [enemy.strip() for enemy in " ".join(args).split(",")]
        await ctx.send(f"The current turn order is: {', '.join(self.enemy_list)}.")
        await asyncio.sleep(5); await ctx.message.delete()
    
    @commands.command()
    async def turn(self, ctx):
        # Increases self.turn_number by 1. Creates an embed from a template.
        self.turn_number += 1
        enemy_list = discord.Embed(
            title = f'Turn #{self.turn_number}',
            color = discord.Color.from_rgb(255, 255, 255))
        enemy_list.set_thumbnail(url = img_enemy_list)
        if self.enemy_list:
            # Checks if self.enemy_list is empty. If it is not, edits enemy_list() with their turn order.
            enemy_list.description = f'Turn Order: \n {", ".join(self.enemy_list)}'
        await ctx.send(embed = enemy_list)
        await asyncio.sleep(5); await ctx.message.delete()
        

# !!!CLASS BELOW IS WIP!!!
class TimeConversion(commands.Cog):
    '''
    This is for the time conversion. Small thing that converts times from UTC in UK/DE time.
    '''
    def __init__(self, bot):
        # Initializes time conversion cog.
        self.bot = bot
        ...
    ...


class Support(commands.Cog):
    '''
    All the support commands. Check strings.py to edit their messages.
    '''
    def __init__(self, bot):
        # Initializes support cog.
        self.bot = bot
    
    @commands.command()
    async def support(self, ctx):
        # Starts the bot help page.
        support = discord.Embed(
            title = 'DNDBot by Daniel',
            description = desc_support,
            color = discord.Color.from_rgb(245, 169, 184))
        support.set_thumbnail(url = img_support)
        await ctx.send(embed = support)
        await asyncio.sleep(5); await ctx.message.delete()
    
    @commands.command()
    async def campaign(self, ctx):
        # Information about the DND campaign.
        campaign = discord.Embed(
            url = doc_campaign,
            title = 'Prometheus',
            description = desc_campaign,
            color = discord.Color.from_rgb(91, 206, 250))
        # Probably could make a for-loop out of the add_field()
        campaign.add_field(name = 'Baughl', value = char_baughl)
        campaign.add_field(name = 'Erhice', value = char_erhice)
        campaign.add_field(name = 'Morgan', value = char_morgan)
        campaign.add_field(name = 'Orange', value = char_orange)
        campaign.add_field(name = 'Tootle', value = char_tootle)
        campaign.add_field(name = 'Ylvie', value = char_ylvie)
        campaign.set_thumbnail(url = img_campaign)
        await ctx.send(embed = campaign)
        await asyncio.sleep(5); await ctx.message.delete()


# TO-DO: add turn_end, initiative, roll
