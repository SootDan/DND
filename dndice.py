import discord, asyncio, random
from discord.ext import commands
from strings import img_enemy_list, desc_support, img_support, desc_campaign, img_campaign, dict_char
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

    @commands.command()
    async def turn_order(self, ctx, *args):
        # Directly affects self.enemy_list.
        self.enemy_list = [enemy.strip() for enemy in " ".join(args).split(",")]
        await ctx.send(f"The current turn order is: {', '.join(self.enemy_list)}.")
        await asyncio.sleep(5); await ctx.message.delete()
    
    @commands.command()
    async def turn_end(self, ctx):
        # Resets self.turn_number and ends combat.
        await ctx.send(f'**Combat ended after {self.turn_number} turns!')
        self.turn_number = 0; self.enemy_list = ''
        await asyncio.sleep(5); await ctx.message.delete()
    
    @commands.command()
    async def roll(self, ctx, arg):
        # Dice rolling command, potentially infinite dice eyes.
        content = arg
        author = ctx.author.id
        # Checks the dict for characters and pronouns, reference strings.py for full list
        character = dict_char[author]['character']
        pronoun = dict_char[author]['pronoun']
        try:
            # Checks if arg is in correct format (e.g. 3d20) and splices it into list.
            content = content.translate(str.maketrans({'d': ' ', '+': ' ', '-': ' '}))
            separator = list(content.split(' ')) # [0] multiplier | [1] eyes | [2] addend

            if not separator[0].isnumeric():
                # Converts multiplier to 1 if none is given
                separator[0] = 1
            
            if not separator[2]:
                # Checks if addend is given. Assign 0 if not.
                separator[2] = 0
            
            # Calculates the roll and adds it to a list that can later be displayed
            rng = [random.randint(1, int(separator[1])) + int(separator[2]) for _ in range(int(separator[0]))]
        
        except:
            msg_error = await ctx.send(f'Invalid input. Did you try the format `!roll XdY+Z`?')
            await asyncio.sleep(5); await ctx.message.delete(); await msg_error.delete()
        
        # Output to user here.
        # This try-except block is because of a Discord limitation where you can only have up to 5000 characters.
        try:
            # will work if message <= 5000
            await ctx.send(f'{character} <@{author}> rolled a {sum(rng)} with {pronoun} {separator[0]}d{separator[1]}+{separator[2]}.`{rng}`')
            await asyncio.sleep(5); await ctx.message.delete()
        
        except:
            # does not print out rng list because of > 5000
            await ctx.send(f'{character} <@{author}> rolled a {sum(rng)} with {pronoun} {separator[0]}d{separator[1]}+{separator[2]}.')

           

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
    
    @commands.command()
    async def initiative(self, ctx):
        # Quick help to roll the dice, useful to sort chat.
        await ctx.send('**Roll for Initiative!**\n*Command:* `!roll d20`')
        await asyncio.sleep(5); await ctx.message.delete()
