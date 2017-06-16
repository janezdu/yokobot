from enum import Enum

class AStren(Enum):
	D = 1000
	C = 1200
	B = 1400
	A = 1600
	S = 1800
	SS = 2000
	F = 0

class Tags(Enum):
	CLASSCH = 1
	MODCH = 2
	EUROP = 3
	WINTER = 4

class Weight(Enum):
	H = 3
	M = 2
	L = 1

class Target:
	def __init__(self, attr, weights, tags):
		self.attributes = [False, False, False, False, False]
		self.weights = [Weight.H, Weight.H, Weight.H, Weight.H, Weight.H]
		# do some typechecking here...
		self.tags = tags


		for i in range(5):
			if len(weights) != 5:
				raise Exception("need to have 5 attributes in a clothing item")
			self.weights[i] = (weights[i])

		for i in range(5):
			if len(attr) != 5:
				raise Exception("need to have 5 attributes in a clothing item")
			self.attributes[i] = (attr[i])

		for x in tags:
			if not isinstance(x, Tags):
				raise TypeError("tags must be set to Tags type")
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

		s = simple+" %d"+lively+" %d"+cute+" %d"+ pure +" %d"+ cool +" %d"
		return s % self.__strengths

	def weightedScore(self, target):
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
# goal = Target(
# 	[True, True, True, True, True],
# 	[Weight.H, Weight.H,Weight.H, Weight.H, Weight.H], 
# 	[Tags.MODCH])

# print(pinky.weightedScore(goal))