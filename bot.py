import discord
from discord.ext import commands
import json
import os

with open ('config.json', 'r', encoding='utf8') as settings:
	config = json.load(settings)
	
bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
	print('>>>System Online<<<')
	print(f'Logged in as: {bot.user.name}')
	print(f'With ID: {bot.user.id}')
	print('Prefix:.')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'Loaded {extension} done')
	
@load.error
async def load_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("You can't do that.\nReason:You are not owner.")
	raise error

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f'cmds.{extension}')
	await ctx.send(f'Unloaded {extension} done')

@unload.error
async def unload_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("You can't do that.\nReason:You are not owner.")
	raise error

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.reload_extension(f'cmds.{extension}')
	await ctx.send(f'Reloaded {extension} done')

@reload.error
async def reload_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("You can't do that.\nReason:You are not owner.")
	raise error

@bot.command()
async def invite(ctx):
	await ctx.send(config['invite'])

@bot.command()
@commands.is_owner()
async def shutdown(parameter_list):
	pass

@shutdown.error
async def shutdown_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("You can't do that.\nReason:You are not owner.")

@bot.command()
@commands.is_owner()
async def reboot(parameter_list):
	pass

@reboot.error
async def reboot_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("You can't do that.\nReason:You are not owner.")

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(config['token'])