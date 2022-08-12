import discord
import random

from discord.ext import commands
from config import config

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

def setup(bot):
	bot.add_cog(memes(bot))
