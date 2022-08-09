import discord
import random
import os

from discord import SlashCommandGroup, Activity
from discord.ext import tasks, commands
from itertools import cycle

#Important Variables:
intents = discord.Intents.default()
intents.message_content = True
#Open the token.txt file (not present in this repository) to obtain the bot's token to enable it to run.
token = open("token.txt", "r").read()
bot = discord.Bot(intents = intents)
statusList = ["Xenoblade Chronicles 3", "The Eternal Now", "The Cycle of Rebirth", "with your lives."]
testGuildList = [927588913466462269, 971409630234296371, 824745963418812476]
#Play event when bot is ready to be used.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}, ID: {bot.user.id}\nMoebius Version: Alpha 0')

#Dumb fucking meme feature because it was funny at the time: (Reply to every message containing "time" with "It's Moebin' time!")
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if "time" in message.content.lower():
        print("Get moebed lmao")
        await message.reply("It's Moebin' time!", mention_author=False)

@tasks.loop(minutes=7)
async def changePresence():
    status = next(bot.statuses)
    await bot.change_presence(activity=discord.Game(name=status))

@changePresence.before_loop
async def waitForReady():
    await bot.wait_until_ready()
    bot.statuses = cycle(statusList)
        
@bot.slash_command()
async def hello(ctx):
    await ctx.respond("Hello, Ouroboros.")

@bot.slash_command()
async def roulette(message):
        i = random.randrange(1, 50)
        author = message.author.display_name
        deathMessages = [f"{author} has blown their own brains out", f"{author} has tripped and fallen onto the trigger", f"{author} won the roulette initially, then got confident and proceeded to try again and blow their own brains out", f"{author} died by their own hand"]
        if i == 7:
            await message.respond(f":gun: {author} has survived the roulette... This time.")
            await message.respond(f"You won't be so lucky next time, {author}", ephemeral=True)
            return
        await message.respond(f":boom: " + random.choice(deathMessages) + ", losing the roulette.")

#Automatically loop through all files in cog directory and make the bot recognise them (Currently commented out because no cogs exist.)
#for cog in os.listdir("./cogs"):
#    if cog.endswith(".py"):
#        print(f"Found {cog}!")
#        cog = f"cogs.{cog.replace('.py', '')}"
#        bot.load_extension(cog)
#        print(f"Loaded {cog} successfully!")

changePresence.start()
bot.run(token)
