file = open("inputday1.txt", "r")
inp = file.read().split()
inpInt = map(int, inp)

tot = sum(map(lambda x: int(x/3) - 2, inpInt))
print(tot)
