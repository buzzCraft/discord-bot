# bot.py
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import ocr_api
import image_reader as img

# Load all tokens from the .env file to avoid the usual fuckups
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set the intents to get the message content
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


# Commands
@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def image(ctx):
    # Test feature to get the image URL
    print(img.get_img_url(ctx))


@bot.command()
async def buck(ctx, added_score: int=0):
    """
    Command to register a Buck score
    :param ctx: discord stuff
    :param scores: Let the user add the score manually
    :return:
    """
    url = await img.get_img_url(ctx)
    score = ocr_api.get_buck_score(url)
    await img.parse_score(ctx, score, added_score, 'Buck')


@bot.command()
async def db_solo(ctx, added_score: int=0):
    """
    Command to register a Deadblocks Solo score
    :param ctx:
    :return:
    """
    url = await img.get_img_url(ctx)
    score = ocr_api.get_db_score(url)
    await img.parse_score(ctx, score, added_score, 'Deadblocks Solo')


bot.run(TOKEN)