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
	"POP": Tags.POP,
	"Winter": Tags.WINTER,
	"Gothic": Tags.GOTHIC,
	"Swordsman": Tags.SWORDS,
	"Army": Tags.ARMY,
	"Military": Tags.ARMY,
	"Kimono": Tags.KIMONO,
	"Floral": Tags.FLORAL,
	"Dancer": Tags.DANCER,
	"Dance": Tags.DANCER,
	"Denim": Tags.DENIM,
	"Fairy": Tags.FAIRY,
	"Evening Gown": Tags.EVGOWN,
	"Lady": Tags.LADY,
	"Rock": Tags.ROCK,
	"Lolita": Tags.LOLITA,
	"Navy": Tags.NAVY,
	"Maiden": Tags.MAIDEN,
	"Shower": Tags.SHOWER,
	"Bunny": Tags.BUNNY,
	"Paramedic": Tags.PARAM,
	"Paramedics": Tags.PARAM,
	"Unisex": Tags.UNISEX,
	"Bohemia": Tags.BOHEMIA,
	"Swimsuit": Tags.SWIMSUIT,
	"Preppy": Tags.PREPPY,
	"Sports": Tags.SPORTS,
	"Homewear": Tags.HOME,
	"Sun Care": Tags.SUN,
	"Chinese Classical": Tags.CHNCLASS,
	"Apron": Tags.APRON,
	"Pet": Tags.PET,
	"Traditional": Tags.TRAD,
	"Goddess": Tags.GODDESS,
	"Britain": Tags.BRITAIN,
	"Office": Tags.OFFICE,
	"Rain": Tags.RAIN,
	"Wedding": Tags.WEDDING,
	"European": Tags.EUROP,
	"Hindu": Tags.HINDU,
	"Pajamas": Tags.PAJAMAS,
	"Republic of China": Tags.REPCHN,
	"Cheongsam": Tags.QIPAO,
	"Korean": Tags.KOREAN,
	"Modern China": Tags.MODCHN,
	"Dryad": Tags.DRYAD,
	"Future": Tags.FUTURE,
	"Futuristic": Tags.FUTURE,
	"Harajuku": Tags.HARAJUKU
}

def rank_clothes(wardrobe, target):
	return sorted(list(wardrobe), 
		key=lambda x: wardrobe[x].weighted_score(target),
		reverse=True)

def load_wardrobe(filename = 'hair.csv'):
	wardrobe = {}
	with open(filename) as csvfile:
		raw = csv.reader(csvfile, delimiter=',')
		for line in raw:
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
		if line[3 + i*2] == '?' or line[4 + i*2] == '?':
			return None
		if line[3 + i*2] == '' and line[4 + i*2] != '':
			attr.append(True)
			stren.append(sdict[line[4 + i*2]])
		elif line[3 + i*2] != '' and line[4 + i*2] == '':
			attr.append(False)
			stren.append(sdict[line[3 + i*2]])
		else:
			return None
	tags = []
	if line[13] != '':
		tags.append(tdict[line[13]])
	if line[14] != '':
		tags.append(tdict[line[14]])

	x = clothing.Clothing(itemnum, name, attr, stren, tags)
	return clothing.Clothing(itemnum, name, attr, stren, tags)


wardrobe = load_wardrobe()
ranking = rank_clothes(wardrobe, clothing.goal)
print([*map(str, ranking)])
