from collections import Counter
crabs = list(map(int, input().split(',')))
crabs.sort()
min_pos = -1
min_fuel = 99999999999999999
for i in range(crabs[0], crabs[-1]+1):
    f = 0
    for c in crabs:
        # f += abs(i-c) # p1
        d = abs(i-c)
        f += (d*d+d)//2
    if f < min_fuel:
        min_fuel = f
        min_pos = i
print(f"{min_pos=}, {min_fuel=}")
