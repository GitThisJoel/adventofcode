import sys
from iteration_utilities import first

b = [list(map(int,l.strip())) for l in sys.stdin]
def get_neighbours(x,y):
    global b
    n = []
    if x-1 >= 0:
        n.append((x-1, y))
    if x+1 < len(b[y]):
        n.append((x+1, y))
    if y-1 > 0:
        n.append((x, y-1))
    if y+1 < len(b):
        n.append((x, y+1))
    return n

def find_lows():
    global b
    s = []
    lows = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            c = b[i][j]
            n = 0
            ok = 0
            if i-1 >= 0:
                n += 1
                if b[i-1][j] > c:
                    ok += 1
            if i+1 < len(b):
                n += 1
                if b[i+1][j] > c:
                    ok += 1
            if j-1 >= 0:
                n += 1
                if b[i][j-1] > c:
                    ok += 1
            if j+1 < len(b[i]):
                n += 1
                if b[i][j+1] > c:
                    ok += 1

            if n == ok:
                s.append(c)
                lows.append((j,i))
    return s, lows

def p1():
    s,_ = find_lows()
    print(sum(s)+len(s))

sizes = []
def p2():
    global b
    _, lowest = find_lows()
    for l in lowest:
        size = 1
        v = {l}
        ns = set(get_neighbours(l[0],l[1]))
        while not len(ns) == 0:
            p = first(ns)
            ns.remove(p)
            if p not in v and b[p[1]][p[0]] >= b[l[1]][l[0]] and b[p[1]][p[0]] < 9:
                size += 1
                v.add(p)
                for neigh in get_neighbours(p[0], p[1]):
                    ns.add(neigh)
        sizes.append(size)
    sizes.sort(reverse = True)
    print(sizes[0]*sizes[1]*sizes[2])
# p1()
p2()
