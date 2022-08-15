import sys
diagram = [[0 for _ in range(1000)] for _ in range(1000)]
# diagram = [[0 for _ in range(11)] for _ in range(11)]
for line in sys.stdin:
    p1,p2 = line.split('->')
    p1 = list(map(int, p1.strip().split(',')))
    p2 = list(map(int, p2.strip().split(',')))

    if p1[0] == p2[0]:
        dir = [0,1] if p1[1] < p2[1] else [0,-1]
        steps = abs(p1[1] - p2[1])
    elif p1[1] == p2[1]:
        dir = [1,0] if p1[0] < p2[0] else [-1,0]
        steps = abs(p1[0] - p2[0])
    else: continue
    p = p1
    for _ in range(steps+1):
        diagram[p[1]][p[0]] += 1
        p[0] += dir[0]
        p[1] += dir[1]
c = 0
for r in diagram:
    for e in r:
        if e > 1:
            c += 1
print(c)
