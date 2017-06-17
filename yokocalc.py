import clothing
from clothing import Tags
from clothing import AStren
import asyncio
import csv 

sdict = {
	"D": AStren.D,
	"C": AStren.C,
	"B": AStren.B,
	"A": AStren.A,
	"S": AStren.S,
	"SS": AStren.SS
}

tdict = {
    "pop":  Tags.POP,
    "winter":  Tags.WINTER,
    "gothic":  Tags.GOTHIC,
    "swordsman":  Tags.SWORDS,
    "army":  Tags.ARMY,
    "military":  Tags.ARMY,
    "kimono":  Tags.KIMONO,
    "floral":  Tags.FLORAL,
    "dancer":  Tags.DANCER,
    "dance":  Tags.DANCER,
    "denim":  Tags.DENIM,
    "fairy":  Tags.FAIRY,
    "evening gown":  Tags.EVGOWN,
    "lady":  Tags.LADY,
    "rock":  Tags.ROCK,
    "lolita":  Tags.LOLITA,
    "navy":  Tags.NAVY,
    "maiden":  Tags.MAIDEN,
    "shower":  Tags.SHOWER,
    "bunny":  Tags.BUNNY,
    "paramedic":  Tags.PARAM,
    "paramedics":  Tags.PARAM,
    "unisex":  Tags.UNISEX,
    "bohemia":  Tags.BOHEMIA,
    "swimsuit":  Tags.SWIMSUIT,
    "preppy":  Tags.PREPPY,
    "sports":  Tags.SPORTS,
    "homewear":  Tags.HOME,
    "sun care":  Tags.SUN,
    "suncare": Tags.SUN,
    "chinese classical":  Tags.CHNCLASS,
    "classical china": Tags.CHNCLASS,
    "classic china": Tags.CHNCLASS,
    "apron":  Tags.APRON,
    "pet":  Tags.PET,
    "traditional":  Tags.TRAD,
    "goddess":  Tags.GODDESS,
    "britain":  Tags.BRITAIN,
    "office":  Tags.OFFICE,
    "rain":  Tags.RAIN,
    "rainy day": Tags.RAIN,
    "wedding":  Tags.WEDDING,
    "european":  Tags.EUROP,
    "europe": Tags.EUROP,
    "hindu":  Tags.HINDU,
    "india": Tags.HINDU,
    "pajamas":  Tags.PAJAMAS,
    "pajama": Tags.PAJAMAS,
    "republic of china":  Tags.REPCHN,
    "cheongsam":  Tags.QIPAO,
    "korean":  Tags.KOREAN,
    "modern china":  Tags.MODCHN,
    "dryad":  Tags.DRYAD,
    "dyrad": Tags.DRYAD,
    "future":  Tags.FUTURE,
    "futuristic":  Tags.FUTURE,
    "近未来": Tags.FUTURE,
    "harajuku":  Tags.HARAJUKU,
    "ethnic": Tags.ETHNIC,
    "エスニック": Tags.ETHNIC
}

def rank_clothes(wardrobe, target):
	return sorted(list(wardrobe), 
		key=lambda x: wardrobe[x].weighted_score(target),
		reverse=True)

def load_wardrobe(filename = 'hair.csv'):
	wardrobe = {}
	with open(filename, encoding='utf-8') as csvfile:
		raw = csv.reader(csvfile, delimiter=',')
		for line in raw:
			if not line[0] in ['1', '2', '3', '4', '5']:
				continue
			newclothing = load_clothing(line)
			if newclothing != None:
				wardrobe[newclothing.name] = newclothing
	return wardrobe

def load_clothing(line):
	star = line[0]
	itemnum = line[1]
	name = line[2]
	attr = []
	stren = []

	for i in range(5):
		if line[3 + i*2] == '' and line[4 + i*2] in sdict:
			attr.append(True)
			stren.append(sdict[line[4 + i*2]])
		elif line[3 + i*2] in sdict and line[4 + i*2] == '':
			attr.append(False)
			stren.append(sdict[line[3 + i*2]])
		else:
			return None


	tags = []

	try:
		if line[13] != '':
			if len( line[13].split(',')) > 1:
				t = line[13].lower().split(',')
				tags.append(tdict[t[0].strip()])
				tags.append(tdict[t[1].strip()])
			else:
				tags.append(tdict[line[13].strip().lower()])
		if line[14] != '':
			tags.append(tdict[line[14].strip().lower()])
	except KeyError as e:
		print("tag error at "+ str(line))

	

	x = clothing.Clothing(itemnum, name, attr, stren, tags)
	return clothing.Clothing(itemnum, name, attr, stren, tags)


# wardrobe = load_wardrobe('wardrobe/dresses.csv')
# ranking = rank_clothes(wardrobe, clothing.goal)
# print([*map(str, ranking)])
