import discord
from discord.ext import commands


class Funs(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print('loaded cog: Funs')


def setup(bot):
	bot.add_cog(Funs(bot))