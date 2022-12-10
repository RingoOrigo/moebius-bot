import discord
import random

from discord.ext import commands
from config import config
from discord import option

class memes(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description = "Declare that it is time to Moeb.")
	async def moeb(self, ctx: discord.ApplicationContext):
		await ctx.respond("IT'S MOEBIN' TIME!")

	@commands.slash_command(description = "Play Russian Roulette, see if you win.")
	async def roulette(self, message):
		i = random.randrange(1, 50)
		author = message.author.display_name
		if i == 7:
			await message.respond(f":gun: {author} has survived the roulette... This time.")
			await message.respond(f"You won't be so lucky next time, {author}.", ephemeral=True)
			return
		await message.respond(f":boom: {author} " + random.choice(config.ROULETTE_DEATH_MESSAGES) + ", losing the roulette.")

	@commands.slash_command(description="Let Moebius decide if you're cool or not.")
	async def cool(self, message):
		coolVal : int = random.randrange(1, 10)
		result = f"```{message.author.display_name}, on a scale of 1 - 10, you get a {coolVal} on the Moebius Cool Meter```\n**|**"
		emote = ""
		
		if (coolVal < 4):
			emote = ":red_square:"
		elif (coolVal < 7):
			emote = ":yellow_square:"
		elif (coolVal < 10):
			emote = ":green_square:"
		elif (coolVal == 10):
			emote = ":blue_square"

		i = 1
		while i<= coolVal:
			result += emote
			i = i + 1
		while coolVal < 10:
			result += ":black_large_square:"
			coolVal = coolVal + 1
		await message.respond(result + "**|**")

def setup(bot):
	bot.add_cog(memes(bot))
