import youtube_dl

ytdl_format_options = {
    'format': 'bestaudio/best',                                     # Best audio quality.
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',            # Download file name.
    'restrictfilenames': False,                                     
    'noplaylist': True,                                             
    'nocheckcertificate': True,                                     # No SSL certificates.
    'ignoreerrors': False,                                          # Stops download when error occurs.
    'logtostderr': False,                                           # Logs error message to file.
    'quiet': True,          
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # IPv4
}

ffmpeg_options = {'options': '-vn'}                                 # Only processes audio.

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)