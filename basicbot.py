import discord
import asyncio
import csv
import yokocalc as yoko
import clothing

hair = yoko.load_wardrobe('hair.csv')
dresses
coats
tops 
bottoms
hosiery
shoes 
accessories
makeup



odict = {
	'simple': (0,True),
	'gorgeous': (0,False),
	'lively': (1, True),
	'elegant': (1,False),
	'cute': (2, True),
	'mature': (2, False),
	'pure': (3, True),
	'sexy': (3, False),
	'cool': (4, True),
	'warm': (4, False),
	's': (0,True),
	'g': (0,False),
	'l': (1, True),
	'e': (1,False),
	'c': (2, True),
	'm': (2, False),
	'p': (3, True),
	'x': (3, False),
	'o': (4, True),
	'w': (4, False)
}

wdict = {
	'h': clothing.Weight.H,
	'high': clothing.Weight.H,
	'm': clothing.Weight.M,
	'medium': clothing.Weight.M,
	'med': clothing.Weight.M,
	'l': clothing.Weight.L,
	'low': clothing.Weight.L
}

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		counter = 0
		tmp = await client.send_message(message.channel, 'Calculating messages...')
		async for log in client.logs_from(message.channel, limit=100):
			if log.author == message.author:
				counter += 1

		await client.edit_message(tmp, 'You have {} messages.'.format(counter))

	elif message.content.startswith('!yoko guide'):
		options = message.content.split()
		target = clothing.Target()
		
		for i in range(len(options)):
			if options[i].lower() in odict and options[i+1].lower() in wdict:
				idx = odict[options[i].lower()][0]
				direc = odict[options[i].lower()][1]
				weight = wdict[options[i+1].lower()]

				target.attributes[idx] = direc
				target.weights[idx] = weight
				i += 1
				
			elif options[i].lower() in yoko.tdict and len(target.tags) < 2:
				tag = clothing.tdict[options[i].lower()]
				target.tags.append(tag)

		choice = "[ERROR] uh oh! Go yell at @cyphra!"
		tmp = await client.send_message(message.channel, 'Calculating outfit...')	
		
		print(target)
		choice = str(yoko.rank_clothes(wr, target)[:5])
		
		await client.edit_message(tmp, 'I recommend... {}'.format(choice))

	elif message.content.startswith('!yoko'):
		await client.send_message(message.channel, "I'll have a yokobot guide soon!")

	elif message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')

client.run('MzI1MzA0ODU1NzcyMjY2NDk3.DCYW4g.TlunK2ZNenVBmtYOz8ogM3NiakI')