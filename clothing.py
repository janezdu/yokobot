from enum import Enum, auto

class AStren(Enum):
	D = 200
	C = 500
	B = 800
	A = 1100
	S = 1400
	SS = 1700
	F = 0

class Tags(Enum):
	POP = auto()
	WINTER = auto()
	GOTHIC = auto()
	SWORDS = auto
	ARMY = auto()
	KIMONO = auto()
	FLORAL = auto()
	DANCER = auto()
	DENIM = auto()
	FAIRY = auto()
	EVGOWN = auto()
	LADY = auto()
	ROCK = auto()
	LOLITA = auto()
	NAVY = auto()
	MAIDEN = auto()
	SHOWER = auto()
	BUNNY = auto()
	PARAM = auto()
	UNISEX = auto()
	BOHEMIA = auto()
	SWIMSUIT = auto()
	PREPPY = auto()
	SPORTS = auto()
	HOME = auto()
	SUN = auto()
	CHNCLASS = auto()
	APRON = auto()
	PET = auto()
	TRAD = auto()
	GODDESS = auto()
	BRITAIN = auto()
	OFFICE = auto()
	RAIN = auto()
	WEDDING = auto()
	EUROP = auto()
	HINDU = auto()
	PAJAMAS = auto()
	REPCHN = auto()
	QIPAO = auto()
	KOREAN = auto()
	MODCHN = auto()
	DRYAD = auto()
	FUTURE = auto()
	HARAJUKU = auto()
	


class Weight(Enum):
	H = 1.7
	M = 1.3
	L = 1
	N = 0

class Target:
	def __init__(self, attr=[], weights=[], tags=[], filt=[]):
		self.attributes = [False, False, False, False, False]
		self.weights = [Weight.N, Weight.N, Weight.N, Weight.N, Weight.N]
		# do some typechecking here...
		self.tags = []
		self.filt = []

		for i in range(len(weights)):
			self.weights[i] = (weights[i])

		for i in range(len(weights)):
			self.attributes[i] = (attr[i])

		for x in tags:
			if not isinstance(x, Tags):
				raise TypeError("tags must be set to Tags type")
			self.tags.append(x)

		for x in filt:
			if not isinstance(x, int):
				raise TypeError("filtered out must be integers")
			self.filt.append(x)

	def __str__(self):
		simple = "simple" if self.attributes[0] else "gorgeous"
		lively = "lively" if self.attributes[1] else "elegant"
		cute = "cute" if self.attributes[2] else "mature"
		pure = "pure" if self.attributes[3] else "sexy"
		cool = "cool" if self.attributes[4] else "warm"

		name = "Target:"
		s = simple+":{d[0]} "+lively+":{d[1]} "+ cute+":{d[2]} "+ pure +":{d[3]} "+ cool +":{d[4]}"
		stats = "{" + s.format(d=self.weights) + "}"
		tags = str([*map(lambda t: t.name, self.tags)])

		return name + "\t\t" + stats + "\t" + tags

class Clothing:
	# trues = simple, lively, cute, pure, cool

	def __init__(self, itemnum, name, attr, stren, tags):
		self.__attributes = [False, False, False, False, False]
		self.__strengths = [AStren.F, AStren.F, AStren.F, AStren.F, AStren.F]
		self.__tags = []
		# do some typechecking here...
		self.id = itemnum
		self.name = name
		for i in range(5):
			if len(stren) != 5:
				raise Exception("need to have 5 attributes in a clothing item")
			self.__strengths[i] = (stren[i].value)

		for i in range(5):
			if len(attr) != 5:
				raise Exception("need to have 5 attributes in a clothing item")
			self.__attributes[i] = (attr[i])

		for x in tags:
			if not isinstance(x, Tags):
				raise TypeError("tags must be set to Tags type")
			self.__tags.append(x)

	def __str__(self):
		simple = "simple" if self.__attributes[0] else "gorgeous"
		lively = "lively" if self.__attributes[1] else "elegant"
		cute = "cute" if self.__attributes[2] else "mature"
		pure = "pure" if self.__attributes[3] else "sexy"
		cool = "cool" if self.__attributes[4] else "warm"

		name = self.name+"(#"+str(self.id) + ")"
		s = simple+":{d[0]} "+lively+":{d[1]} "+ cute+":{d[2]} "+ pure +":{d[3]} "+ cool +":{d[4]}"
		stats = "{" + s.format(d=self.__strengths) + "}"
		tags = str([*map(lambda t: t.name, self.__tags)])

		return name + "\t\t" + stats + "\t" + tags

	def weighted_score(self, target):
		if self.id in target.filt:
			return 0
		score = 0
		for i in range(5):
			value = self.__strengths[i] * target.weights[i].value
			for targetTag in target.tags:
				if targetTag in self.__tags:
					value *= 3
			if target.attributes[i] ^ self.__attributes[i]:
				value *= -1
			score += value
		return score

# pinky = Clothing(2, "Nikki's Pinky", 
# 	[True, True, True, True, True],
# 	[AStren.S, AStren.D, AStren.S, AStren.A, AStren.B],
# 	[Tags.EUROP])
goal = Target(
	[True, True, True, True, True],
	[Weight.H, Weight.H,Weight.H, Weight.H, Weight.H], 
	[Tags.MODCHN], [])
# print(pinky)
# print(pinky.weightedScore(goal))