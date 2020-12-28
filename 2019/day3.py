file = open("inputday3.txt", "r")
inp = file.read().split()
first  = inp[0].split(",")
second = inp[1].split(",")

def calcDist(p):
    return abs(p[0]) + abs(p[1])

pos = (0, 0)
allFirstPos = set()

for d in first:
    dir = d[0]
    l = int(d[1:])
    if dir == "U":
        for i in range(l):
            pos = (pos[0], pos[1]+1)
            allFirstPos.add(pos)
    elif dir == "D":
        for i in range(l):
            pos = (pos[0], pos[1]-1)
            allFirstPos.add(pos)
    elif dir == "R":
        for i in range(l):
            pos = (pos[0]+1, pos[1])
            allFirstPos.add(pos)
    else:
        for i in range(l):
            pos = (pos[0]-1, pos[1])
            allFirstPos.add(pos)

best = 99999999999999999999
pos = (0, 0)
for d in second:
    dir = d[0]
    l = int(d[1:])
    if dir == "U":
        for i in range(l):
            pos = (pos[0], pos[1]+1)
            if pos in allFirstPos:
                best = min(calcDist(pos), best)
    elif dir == "D":
        for i in range(l):
            pos = (pos[0], pos[1]-1)
            if pos in allFirstPos:
                best = min(calcDist(pos), best)
    elif dir == "R":
        for i in range(l):
            pos = (pos[0]+1, pos[1])
            if pos in allFirstPos:
                best = min(calcDist(pos), best)
    else:
        for i in range(l):
            pos = (pos[0]-1, pos[1])
            if pos in allFirstPos:
                best = min(calcDist(pos), best)
print(best)
