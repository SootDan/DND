import discord, asyncio
from os import listdir # Soundboard check.
from os.path import isfile, join # Useful for soundboard check only.
from discord.ext import commands
from dndice import bot_return
from youtube_init import ffmpeg_options, ytdl

# Initalizes bot config.
intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '!', intents = intents)

# WIP!!!
class Music(discord.PCMVolumeTransformer):
    '''
    Takes care of sound files and streams from the internet.
    '''
    def __init__(self, source, *, data, volume = 1):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    
    @classmethod
    async def url_fetch(cls, url, *, loop = None, stream = False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download = not stream))
        
        if 'entries' in data:
            # Takes first item from playlist.
            data = data['entries'][0]
        
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data = data)
 
    
class Voice(commands.Cog):
    '''
    This makes the bot recognise when somebody is in voice chat and enters it.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def connect(self, ctx):
        # Joins the voice channel a user is currently in.
        voice = ctx.author.voice
        if voice is None:
            await bot_return(ctx, f'Please connect to a voice channel first.')
        elif ctx.voice_client is not None:
            await ctx.voice_client.move_to(voice.channel)
            await bot_return(ctx, f'Switching to {voice.channel}.')
        else:
            await voice.channel.connect()
            await bot_return(ctx, f'Connecting to {voice.channel}.')

    @commands.command()
    async def disconnect(self, ctx):
        # Disconnects bot from voice chat.
        await ctx.voice_client.disconnect()
        await bot_return(ctx, 'Disconnecting. Goodbye!')
    
    @commands.command()
    async def stream(self, ctx, *, url):
        # Streams from URL.
        soundfile = await Music.url_fetch(url, loop = self.bot.loop)
        ctx.voice_client.play(soundfile)
        await bot_return(ctx, f'Good choice! Now playing: {soundfile.title}')
    
    @commands.command()
    async def soundboard(self, ctx, *, query):
        # Plays a soundboard file.
        file = query.lower()
        # Files are stored under Soundboard/ and are all .mp3.
        if not file.startswith('Soundboard/'):
            file = 'Soundboard/' + file
        if not file.endswith('.mp3'):
            file = file + '.mp3'

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
        ctx.voice_client.play(source)
        await bot_return(ctx, f'Playing soundboard file: {query}')
    
    @commands.command()
    async def soundboard_list(self, ctx):
        # Lists all available sound files in Soundboard/ for users.
        soundboard_files = [f for f in listdir('Soundboard/') if isfile(join('Soundboard', f))]
        for file in soundboard_files:
            ... # WIP: Change it so it will not display .mp3 anymore.
        await bot_return(ctx, f'The currently available sound files are: \n{soundboard_files}')
        
    @commands.command()
    async def volume(self, ctx, volume: int):
        # Changes output volume.
        ctx.voice_client.source.volume = volume / 100
        await bot_return('Changed voice chat volume.')
        # WIP