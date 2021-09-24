import os
import json
async def login(prefix, api, message):
	if not os.path.exists("accounts/"+str(message.author.id)+".json"):
				if len(message.content) == 7:
					await message.channel.send("please enter a tag")
				else:
					msg = message.content
					r = msg.replace(prefix+"login", "")
					a = r.replace("#", "")
					tag = a.replace(" ", "")
					try:
						check = await message.channel.send("verifying tag...")
						api.get_player(tag)
						exists = True
					except:
						exists = False
					if exists:
						f = open(f"accounts/{str(message.author.id)}.json", "w")
						data = {"tag": tag}
						json.dump(data, f)
						f.close()
						await message.channel.send("succesfully logged in as **"+api.get_player(tag)["name"]+"**.")
						await check.delete()
					else:
						await message.channel.send("account with the provided tag was not found.")
						await check.delete()
	else:
		await message.channel.send("you are already logged in.")
