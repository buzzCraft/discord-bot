
import discord


async def get_img_url(ctx):
    """
    Function to get the image URL from the last message in the channel
    :param ctx: discord stuff
    :return:
    """
    if isinstance(ctx.channel, discord.TextChannel):
        async for message in ctx.channel.history(limit=10):
            if len(message.attachments) > 0:
                image_url = message.attachments[0].url
                return image_url
        else:
            return None

async def parse_score(ctx, score, added_score, game):
    """
    Function to handle the score verification
    :param ctx: discrod stuff
    :param score: read from ocr
    :param added_score: inputed by user
    :param game: name of the game
    :return:
    """
    try:
        score = int(score.strip().replace(" ", ""))
    except ValueError:
        # Add some logging here
        pass

    if score == added_score:
        await ctx.send(f'Verified score of {score} added by {ctx.author} in {game}')
    else: # When image score doesn't match user input - do something fun!?!
        await ctx.send(f'User input {added_score}, read from image: {score} in {game}')