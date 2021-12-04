import sys

numbers = list(map(int, input().split(',')))
number_set = set(numbers)
input() # empty line


min_round = len(numbers)
score = 0
board = []

def bingo(b):
    global min_round
    rac = [r.copy() for r in b]

    for i in range(len(board[0])):
        rac.append([x[i] for x in board])

    bs = [set(e) for e in rac]
    ns = set()
    for k in range(min_round):
        ns.add(numbers[k])
        for e in bs:
            if e.issubset(ns):
                # bingo found
                sum = 0
                for i in range(len(b)):
                    for j in range(len(b[i])):
                        if not b[i][j] in ns:
                            sum += b[i][j]
                new_score = sum * numbers[k]
                min_round = k
                return new_score
    return -1

for line in sys.stdin:
    line = line.strip()
    if len(board) == 5:
        # reset board and score
        new_score = bingo(board)
        if new_score > -1:
            score = new_score
        board = []
    else:
        board.append(list(map(int, line.split())))
new_score = bingo(board)
if new_score > -1:
    score = new_score
print(score)
exit(0)
