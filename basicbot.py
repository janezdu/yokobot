import discord
import asyncio
import csv
import yokocalc as yoko
import clothing

hair = yoko.load_wardrobe('wardrobe/hair.csv')
dresses = yoko.load_wardrobe('wardrobe/dresses.csv')
coats = yoko.load_wardrobe('wardrobe/coats.csv')
tops = yoko.load_wardrobe('wardrobe/tops.csv')
bottoms = yoko.load_wardrobe('wardrobe/bottoms.csv')
hosiery = yoko.load_wardrobe('wardrobe/hosiery.csv')
shoes = yoko.load_wardrobe('wardrobe/shoes.csv')
accessories = yoko.load_wardrobe('wardrobe/accessories.csv')
makeup = yoko.load_wardrobe('wardrobe/makeup.csv')



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
			if options[i].lower() in odict and i < len(options)-1 and options[i+1].lower() in wdict:
				idx = odict[options[i].lower()][0]
				direc = odict[options[i].lower()][1]
				weight = wdict[options[i+1].lower()]

				target.attributes[idx] = direc
				target.weights[idx] = weight
				
			elif options[i].lower() in yoko.tdict and len(target.tags) < 2:
				tag = yoko.tdict[options[i].lower()]
				target.tags.append(tag)

		choice = "[ERROR] uh oh! Go yell at @cyphra!"
		tmp = await client.send_message(message.channel, 'Calculating outfit...')	
		
		print(target)
		cHair = str(yoko.rank_clothes(hair, target)[:5])
		cDress = str(yoko.rank_clothes(dresses, target)[:5])
		cCoats = str(yoko.rank_clothes(coats, target)[:5]) 
		cTops = str(yoko.rank_clothes(tops, target)[:5])
		cBott = str(yoko.rank_clothes(bottoms, target)[:5])
		cHosi = str(yoko.rank_clothes(hosiery, target)[:5])
		cShoes = str(yoko.rank_clothes(shoes, target)[:5])
		cMakeup = str(yoko.rank_clothes(makeup, target)[:5])

		
		await client.edit_message(tmp, 
			"""I recommend... \n
			Hair: \t{}\n
			Dress: \t{}\n
			Coats: \t{}\n
			Tops: \t{}\n
			Bottoms: \t{}\n
			Hosiery: \t{}\n
			Shoes: \t{}\n
			Makeup: \t{}\n 
			""".format(cHair, cDress, cCoats, cTops, cBott, cHosi, cShoes, cMakeup))

	elif message.content.startswith('!yoko'):
		await client.send_message(message.channel, "I'll have a yokobot guide soon!")

	elif message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')

client.run('MzI1MzA0ODU1NzcyMjY2NDk3.DCYW4g.TlunK2ZNenVBmtYOz8ogM3NiakI')