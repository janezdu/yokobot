import clothing
import asyncio
import csv 

sdict = {
    "D": clothing.AStren.D,
    "C": clothing.AStren.C,
    "B": clothing.AStren.B,
    "A": clothing.AStren.A,
    "S": clothing.AStren.S,
    "SS": clothing.AStren.SS
}

def loadWardrobe(filename = 'hair.csv'):
    wardrobe = []
    with open(filename) as csvfile:
        raw = csv.reader(csvfile, delimiter=',')
        for line in raw:
            newclothing = loadClothing(line)
            if newclothing != None:
                wardrobe.append(newclothing)


def loadClothing(line):
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
        tags.append(line[13])
    if line[14] != '':
        tags.append(line[14])

loadWardrobe()