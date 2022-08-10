
import discord
import random
import os

from discord import SlashCommandGroup, Activity
from discord.ext import tasks, commands
from itertools import cycle
from config import config

#Important Variables:
intents = discord.Intents.default()
intents.message_content = True
#Open the token.txt file (not present in this repository) to obtain the bot's token to enable it to run.
bot = discord.Bot(intents = intents)
statusList = ["Xenoblade Chronicles 3", "The Eternal Now", "The Cycle of Rebirth", "with your lives."]

#Play event when bot is ready to be used.
@bot.event
async def on_ready():
    print(config.START_MESSAGE)

#Dumb fucking meme feature because it was funny at the time: (Reply to every message containing "time" with "It's Moebin' time!")
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if "time" in message.content.lower():
        await message.reply("It's Moebin' time!", mention_author=False)

@tasks.loop(minutes=7)
async def changePresence():
    status = random.choice(config.STATUS_LIST)
    await bot.change_presence(activity=discord.Game(name=status))

@changePresence.before_loop
async def waitForReady():
    await bot.wait_until_ready()
        
@bot.slash_command()
async def hello(ctx):
    await ctx.respond("Hello, Ouroboros.", ephemeral=True)

#Automatically loop through all files in cog directory and make the bot recognise them (Currently commented out because no cogs exist.)
for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        print(config.COG_LOAD)
        cog = f"cogs.{cog.replace('.py', '')}"
        bot.load_extension(cog)
        print(config.COG_SUCCESS)

changePresence.start()
bot.run(config.BOT_TOKEN)
