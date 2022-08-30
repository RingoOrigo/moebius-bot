import discord
import random

from discord.ext import commands
from config import config
from discord import option

class socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Hug another user within this server")
    @option("User to Hug", discord.Member, description = "Select the user that you wish to hug", required = True)
    async def hug(self, message, member: discord.Member):
        embed = discord.Embed(
            title = f"{message.author.display_name} has hugged {member.display_name}",
            description = random.choice(config.POSITIVE_COMMUNITY_MESSAGES),
            color = discord.Colour.red()
        )
        embed.set_image(url=random.choice(config.HUG_GIF_LINKS))
        await message.respond(embed=embed)

    @commands.slash_command(description="Pat another user in this server on the head")
    @option("User to pat", discord.Member, description = "Select the user's head you wish to pat", required = True)
    async def pat(self, message, member: discord.Member):
        embed = discord.Embed(
            title = f"{message.author.display_name} has given {member.display_name} a pat on the head",
            description = random.choice(config.POSITIVE_COMMUNITY_MESSAGES),
            color = discord.Colour.red()
        )
        embed.set_image(url=random.choice(config.HEAD_PAT_GIF_LINKS))
        await message.respond(embed=embed)
    
def setup(bot):
    bot.add_cog(socials(bot))
