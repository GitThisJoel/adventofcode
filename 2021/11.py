import sys
lx = 0
ly = 0
board = []

def get_neighbours(p):
    x = p[0]; y = p[1]
    global lx
    global ly
    ns = []
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if 0 <= y+dy < ly and 0 <= x+dx < lx and not dx == dy == 0:
                ns.append((x+dx, y+dy))
    return ns

def update_neighbours(pos):
    global board
    n = set()
    for p in get_neighbours(pos):
        board[p[1]][p[0]] += 1
        if board[p[1]][p[0]] == 10:
            n.add(p)
            n = set.union(n, update_neighbours(p))
    return n

def p1():
    global board
    flashes = 0
    for _ in range(1,101):
        nines = set()
        for i in range(ly):
            for j in range(lx):
                board[i][j] += 1
                if board[i][j] == 10:
                    nines.add((i,j))
                    nines = set.union(nines, update_neighbours((j,i)))
        # flashes += len(nines)
        # for p in nines:
            # board[p[1]][p[0]] = 0
        for i in range(ly):
            for j in range(lx):
                if board[i][j] > 9:
                    flashes += 1
                    board[i][j] = 0
    print(flashes)
    return

def p2():
    global board
    r = 1
    while(True):
        flashes = 0
        nines = set()
        for i in range(ly):
            for j in range(lx):
                board[i][j] += 1
                if board[i][j] == 10:
                    nines.add((i,j))
                    nines = set.union(nines, update_neighbours((j,i)))
        # flashes += len(nines)
        # for p in nines:
            # board[p[1]][p[0]] = 0
        for i in range(ly):
            for j in range(lx):
                if board[i][j] > 9:
                    flashes += 1
                    board[i][j] = 0
        if flashes == lx*ly:
            print(r)
            return
        r += 1
    return


if __name__ == "__main__":
    board = [list(map(int, l.strip())) for l in sys.stdin]
    ly = len(board)
    lx = len(board[0])
    p2()
