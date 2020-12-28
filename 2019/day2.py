file = open("inputday2.txt", "r")
inp = file.read().split(",")
nbrs = list(map(int, inp))

nbrs[1] = 12
nbrs[2] = 2
quit = False
i = 0
while not quit:
    op = nbrs[i]
    if op == 99:
        quit = True
    elif op == 1: # addition
        ind1 = nbrs[i+1]
        ind2 = nbrs[i+2]
        dest = nbrs[i+3]
        nbrs[dest] = nbrs[ind1] + nbrs[ind2]
    elif op == 2: # multiplication
        ind1 = nbrs[i+1]
        ind2 = nbrs[i+2]
        dest = nbrs[i+3]
        nbrs[dest] = nbrs[ind1] * nbrs[ind2]
    else:
        print("error")
    i += 4

print(nbrs[0])
