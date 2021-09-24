import os
import json
async def profile(config, prefix, api, message):
	if message.mentions:
		user = str(message.content).replace("@", "")
		user = user.replace("<", "")
		user = user.replace(">", "")
		user = user.replace(prefix+"profile", "")
		user = user.replace(" ", "")
	if not message.mentions:
		path = "accounts/"+str(message.author.id)+".json"
	else:
		path = "accounts/"+str(user)+".json"
	if not os.path.exists(path):
		if message.mentions:
			await message.channel.send(f"This user is not logged in.\nuse `{prefix}login <tag>` to login.")
		else:
			await message.channel.send(f"You are not loghed in.\nuse `{prefix}login` <tag> to login.")
	else:
		o = open(f"accounts/{str(message.author.id)}.json", "r")
		o_data = o.read()
		o.close()
		acc_data = json.loads(o_data)
		tag = acc_data["tag"]
		player = api.get_player(tag)
		unlocked_brawlers = []
		for brawler_id in range(len(player["brawlers"])):
			b_name = player["brawlers"][brawler_id]["name"]
			unlocked_brawlers.append(b_name.lower())
		string = str(unlocked_brawlers)
		string1 = string.replace("[", "")
		string2 = string1.replace("]", "")
		brawlers_list = string2.replace("'", "")
		brawlers_count = config['total_brawlers=count']
		await message.channel.send(f"**__name:__** {player['name']}\n**__tag:__** #{tag}\n**__{config['trp']} trophies:__** {player['trophies']}\n**__{config['trp']} highest trophies:__** {player['highest_trophies']}\n**__{config['xp']} exp level:__** {player['exp_level']}\n**__{config['xp']} exp points:__** {player['exp_points']}\n**__{config['3vs3']} 3vs3 victories:__** {player['3vs3_victories']}\n**__{config['duo']} duo showdown victories:__** {player['duo_victories']}\n**__{config['solo']} solo showdown victories:__** {player['solo_victories']}\n**__{config['club']} club name:__** {player['club']['name']}\n**__{config['club']} club tag:__** {player['club']['tag']}\n**__{config['brawlers']} unlocked brawlers:__** **__`[{len(player['brawlers'])}/{brawlers_count}]`__**")
