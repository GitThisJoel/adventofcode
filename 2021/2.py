import sys
p = [0,0]
aim = 0
depth = 0
for line in sys.stdin:
    d,n = line.split()
    n = int(n)
    if d == "forward":
        p[0] += n
        depth += n*aim
    elif d == "down":
        p[1] += n
        aim += n
    elif d == "up":
        p[1] -= n
        aim -= n
# part 1
# print(p[0]*p[1])
# part 2
print(p[0]*depth)
