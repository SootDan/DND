import discord, asyncio, random, pytz
from discord.ext import commands
from datetime import datetime, timedelta
from strings import desc_campaign, desc_support, desc_timer, dict_char
from strings import img_campaign, img_enemy_list, img_support, img_timer
from privatefiles import doc_campaign, char_baughl, char_erhice, char_morgan, char_orange, char_tootle, char_ylvie

# Initalizes bot config.
intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '!', intents = intents)

async def bot_return(ctx, *args, **kwargs):
    # Small function to add to each command, returns output and deletes input after a delay.
    output = await ctx.send(*args, **kwargs)
    await asyncio.sleep(5); await ctx.message.delete()
    return output

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
        await bot_return(ctx, embed = enemy_list)

    @commands.command()
    async def turn_order(self, ctx, *args):
        # Directly affects self.enemy_list.
        self.enemy_list = [enemy.strip() for enemy in ' '.join(args).split(',')]
        await bot_return(ctx, f'The current turn order is: {", ".join(self.enemy_list)}.')
    
    @commands.command()
    async def turn_end(self, ctx):
        # Resets self.turn_number and ends combat.
        await bot_return(ctx, f'**Combat ended after {self.turn_number} turns!**')
        self.turn_number = 0; self.enemy_list = ''
    
    async def roll_output(self, ctx, arg, dice_type = 0):
        # Performs a Dungeons & Dragons dice roll.
        # This function is not called by a user and serves as a calculator for the actual input commands below.
        # Dice type parameters: 0: Standard, 1: Advantage, 2: Disadvantage
        content = arg
        author = ctx.author.id
        character = dict_char[author]['character']                          # Sets character as defined by UUID.
        pronoun = dict_char[author]['pronoun']                              # Finds custom pronoun set as applicable.
        
        try:
            content = content.translate(str.maketrans({'d': ' ', '+': ' ', '-': ' -'}))
            separator = list(content.split(' '))                            # [0] Multiplier | [1] Eyes | [2] Addend
            # Handles multiplier of dice, checks which dice type it is
            separator[0] = 1 if dice_type == 0 and not separator[0].isnumeric() else 2 if dice_type > 0 else separator[0]   
            separator.append(0) if len(separator) < 3 else None             # Adds +0 if no addend is given.

            # Calculates the roll and adds it to a list as output. 
            rng = [random.randint(1, int(separator[1])) + int(separator[2]) for _ in range(int(separator[0]))]
            addend_sign = '+' if int(separator[2]) >= 0 else ''             # Changes addend sign in the output if >= 0.
            output_msg = ['standard', 'advantage', 'disadvantage']
            result = [sum(rng), max(rng), min(rng)]

            # Output to user here. Respects Discord limitations of up to 5000 characters by removing list if > 5000.
            try:
                await bot_return(ctx, f'{character} rolled a **{result[dice_type]}** with {pronoun} {output_msg[dice_type]} roll! `{separator[0]}d{separator[1]}{addend_sign}{separator[2]} | {rng}`')
            except:
                await bot_return(ctx, f'{character} rolled a **{result[dice_type]}** with {pronoun} {output_msg[dice_type]} roll! `{separator[0]}d{separator[1]}{addend_sign}{separator[2]}`')

        except:
            roll_types = ['roll XdY+Z', 'advantage dY+Z', 'disadvantage dY+Z']
            msg_error = 'Invalid input. Did you try the format `!' + roll_types[dice_type] + '`?'
            await bot_return(ctx, msg_error)
    
    @commands.command()
    async def roll(self, ctx, arg):
        # Standard roll with an infinite possibility of input choices, e.g. 99d999+99.
        await self.roll_output(ctx, arg, dice_type = 0)
    
    @commands.command()
    async def advantage(self, ctx, arg):
        # Advantage roll. Always chooses higher of two dice rolls.
        await self.roll_output(ctx, arg, dice_type = 1)
    
    @commands.command()
    async def disadvantage(self, ctx, arg):
        # Disadvantage roll. Always chooses lower of two dice rolls.
        await self.roll_output(ctx, arg, dice_type = 2)


class TimeConversion(commands.Cog):
    '''
    This is for the time conversion. Small thing that converts times from UTC in UK/DE time.
    '''
    def __init__(self, bot):
        # Initializes time conversion cog.
        self.bot = bot
        self.time_zones = [pytz.timezone('Europe/London'), pytz.timezone('Europe/Berlin')]

    @commands.command()
    async def utc(self, ctx, arg):
        # Converts dates from UTC into B(S)T and CE(S)T. Automatically checks if DST applies.
        content = str(arg)
        current_date = datetime.now()
        # Checks if DST is True for either time zone.
        dst = [zone.dst(current_date) != timedelta(0) for zone in self.time_zones]
        # Now takes UTC input and formats. Checks if utc input is either '18' (18:00) or '1830' (18:30).
        utc_time = datetime.strptime(content, '%H%M' if len(content) == 4 else '%H').time()
        bt_hour = utc_time.hour + 1 if dst[0] else utc_time.hour
        cet_hour = utc_time.hour + 2 if dst[1] else utc_time.hour + 1
        uni_minute = utc_time.minute if len(content) == 4 else 0 # Checks if minute is given, sets to 0 otherwise.

        british_time = current_date.astimezone(self.time_zones[0]).replace(hour = bt_hour, minute = uni_minute)
        european_time = current_date.astimezone(self.time_zones[1]).replace(hour = cet_hour, minute = uni_minute)
        
        timer_list = discord.Embed(
            title = f'{utc_time} UTC is:',
            description = desc_timer.format(british_time.strftime('%H:%M'), european_time.strftime('%H:%M')),
            color = discord.Color.from_rgb(156, 89, 209))
        timer_list.set_thumbnail(url = img_timer)
        await bot_return(ctx, embed = timer_list)
        
        
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
        await bot_return(ctx, embed = support)
    
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
        await bot_return(ctx, embed = campaign)
    
    @commands.command()
    async def initiative(self, ctx):
        # Quick help to roll the dice, useful to sort chat.
        await bot_return(ctx, '**Roll for Initiative!**\n*Command:* `!roll d20`')