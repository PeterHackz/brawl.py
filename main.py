# import built-in modules
import json
import os
# import custom modules
import discord
import brawlstats
from discord.ext import commands
# setting up bot, some people name it as "client"
bot = commands.Bot(command_prefix="unused_prefix") # since I used "on_message" to make and load commands, the bot won't use this as a prefix
# getting config data
o = open("tools/config.json", "r")
o_data = o.read()
o.close()
bot_data = json.loads(o_data)
# setting up the brawlstats module
api = brawlstats.Client(bot_data["api_key"])
# import commands
from commands.login import login
from commands.profile import profile
# start the event
@bot.event
async def on_message(message):
	prefix = "!!"
	b = open("tools/blacklist.json", "r")
	blacklist = json.loads(b.read())
	b.close() # loading blacklist file data on each message to make it possible to blacklist users without restarting the bot
	if message.author.bot:# checking if user is bot, if yes, it will be ignored when a command is called
		pass
	elif message.author.id in blacklist['ids']:# checking if user is blacklisted
		pass
	elif message.content.lower().startswith(prefix+"login"):
		await login(prefix, api, message)
	elif message.content.lower().startswith(prefix+"profile"):
		await profile(bot_data, prefix, api, message)
print("running...")
bot.run(bot_data["bot_token"])
