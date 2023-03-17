# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import api_test


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
active_channel_ids = []



@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def image(ctx):
    if active_channel_ids:
        found_image = False
        for channel_id in active_channel_ids:
            channel = bot.get_channel(channel_id)
            if isinstance(channel, discord.TextChannel):
                async for message in channel.history(limit=10):
                    if len(message.attachments) > 0:
                        image_url = message.attachments[0].url
                        await ctx.send(f'The URL of the image is: {image_url}')
                        found_image = True
                        break

            if found_image:
                break

        if not found_image:
            await ctx.send('No images found in the active channels.')
    else:
        await ctx.send('No active channels set. Use /addchannel to add channels.')

@bot.command()
async def buck(ctx):
    if active_channel_ids:
        found_image = False
        for channel_id in active_channel_ids:
            channel = bot.get_channel(channel_id)
            if isinstance(channel, discord.TextChannel):
                async for message in channel.history(limit=10):
                    if len(message.attachments) > 0:
                        image_url = message.attachments[0].url
                        score = api_test.get_buck_score(image_url)
                        await ctx.send(f'Score of: {score } is registered for user: {ctx.author} in Buck')
                        found_image = True
                        break

            if found_image:
                break

        if not found_image:
            await ctx.send('No images found in the active channels.')
    else:
        await ctx.send('No active channels set. Use /addchannel to add channels.')

@bot.command()
async def db_solo(ctx):
    if active_channel_ids:
        found_image = False
        for channel_id in active_channel_ids:
            channel = bot.get_channel(channel_id)
            if isinstance(channel, discord.TextChannel):
                async for message in channel.history(limit=10):
                    if len(message.attachments) > 0:
                        image_url = message.attachments[0].url
                        score = api_test.get_db_score(image_url)
                        await ctx.send(f'Score of: {score } is registered for user: {ctx.author} in DeadBlocks Solo')
                        found_image = True
                        break

            if found_image:
                break

        if not found_image:
            await ctx.send('No images found in the active channels.')
    else:
        await ctx.send('No active channels set. Use /addchannel to add channels.')

@bot.command()
async def addchannel(ctx, channel: discord.TextChannel):
    if channel.id not in active_channel_ids:
        active_channel_ids.append(channel.id)
        await ctx.send(f'{channel.mention} added to active channels.')
    else:
        await ctx.send(f'{channel.mention} is already in active channels.')

@bot.command()
async def removechannel(ctx, channel: discord.TextChannel):
    if channel.id in active_channel_ids:
        active_channel_ids.remove(channel.id)
        await ctx.send(f'{channel.mention} removed from active channels.')
    else:
        await ctx.send(f'{channel.mention} is not in active channels.')

@bot.command()
async def listchannels(ctx):
    if active_channel_ids:
        channels = [bot.get_channel(channel_id).mention for channel_id in active_channel_ids]
        await ctx.send(f'The active channels are: {" | ".join(channels)}')
    else:
        await ctx.send('No active channels set. Use /addchannel to add channels.')



bot.run(TOKEN)