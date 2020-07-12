import discord
from discord.ext import commands
import datetime


class Utilities(commands.Cog):
	def __init__(self, bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('loaded cog: Utilities')

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'pong @ {round(self.bot.latency*1000)} ms')


def setup(bot):
	bot.add_cog(Utilities(bot))