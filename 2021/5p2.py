import sys
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def get_dir(p1,p2):
    dir = [p2[0] - p1[0], p2[1] - p1[1]]
    d=gcd(dir[0],dir[1])
    dir = [dir[0]/d, dir[1]/d]
    assert dir[0] == int(dir[0])
    assert dir[1] == int(dir[1])

    if p1[0] < p2[0]:
        dir[0] = abs(dir[0])
    elif p1[0] > p2[0]:
        dir[0] = -abs(dir[0])

    if p1[1] < p2[1]:
        dir[1] = abs(dir[1])
    elif p1[1] > p2[1]:
        dir[1] = -abs(dir[1])
    return [int(k) for k in dir]

diagram = [[0 for _ in range(1000)] for _ in range(1000)]
# diagram = [[0 for _ in range(11)] for _ in range(11)]
for line in sys.stdin:
    p1,p2 = line.split('->')
    p1 = list(map(int, p1.strip().split(',')))
    p2 = list(map(int, p2.strip().split(',')))

    dir = get_dir(p1,p2)
    while not p1 == [p2[0] + dir[0], p2[1] + dir[1]]:
        diagram[p1[1]][p1[0]] += 1
        p1[0] += dir[0]
        p1[1] += dir[1]

c = 0
for r in diagram:
    for e in r:
        if e > 1:
            c += 1
print(c)
