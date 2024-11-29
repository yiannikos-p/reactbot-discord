# Replace 'YOUR_BOT_TOKEN' with your bot's token
import discord
from discord.ext import commands
import os
import random
import sys

# Replace this with your bot token
TOKEN = sys.argv[1]

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read the content of messages
intents.guilds = True  # Required for guild-related events like voice channel connections
intents.voice_states = True  # Required for voice state management

# Create bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Directory containing MP3 files
AUDIO_DIR = sys.argv[2] 

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='join')
async def join(ctx):
    """Joins the voice channel of the user who invoked the command."""
    if ctx.author.voice:  # Check if the user is in a voice channel
        channel = ctx.author.voice.channel
        await channel.connect()  # Join the user's voice channel
        await ctx.send(f"Joined {channel.name}!")
    else:
        await ctx.send("You are not in a voice channel.")

@bot.command(name='leave')
async def leave(ctx):
    """Leaves the voice channel."""
    if ctx.voice_client:  # Check if the bot is in a voice channel
        await ctx.voice_client.disconnect()  # Disconnect from the voice channel
        await ctx.send("Left the voice channel!")
    else:
        await ctx.send("I'm not in a voice channel.")

@bot.command(name='react')
async def react(ctx):
    """Plays a random MP3 file from the directory."""
    if ctx.voice_client:  # Check if the bot is in a voice channel
        if ctx.voice_client.is_playing():
            await ctx.send("I'm already playing something!")
            return

        # Get a random MP3 file from the directory
        files = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.mp3')]
        if not files:
            await ctx.send("No audio files found in the directory!")
            return

        random_file = random.choice(files)
        file_path = os.path.join(AUDIO_DIR, random_file)

        # Play the MP3 file
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path))
        await ctx.send(f"Playing: {random_file}")
    else:
        await ctx.send("I'm not in a voice channel! Use `!join` first.")

# Run the bot
bot.run(TOKEN)

