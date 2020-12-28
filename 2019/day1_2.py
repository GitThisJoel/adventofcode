file = open("inputday1pt2.txt", "r")
inp = file.read().split()
inpInt = map(int, inp)

def calc(x):
    return int(x/3) - 2

def fuel(m):
    x   = calc(m)
    tot = x
    while(x > 0):
        temp = calc(x)
        if temp > 0:
            tot += temp
            x = temp
        else:
            break
    return tot

total = sum(map(lambda x: fuel(x), inpInt))
# total = 0
# for nbr in inpInt:
#     total += fuel(nbr)

print(total)
