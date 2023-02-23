import sys

sys.path.extend([".", ".."])

from utils import *

xshift = 175
xrowlength = 500
xsource = 500 - xshift
board = []


def insert_board(x, y, c="#"):
    global board
    if len(board) <= y:
        for _ in range(y - len(board) + 1):
            board.append(["." for _ in range(xrowlength)])
    # print(x, y, "len board:", len(board[0]), len(board))
    board[y][x - xshift] = c


def prepare_board(lines):
    global board
    board = [["." for _ in range(xrowlength)] for _ in range(1)]
    for segment in lines:
        points = list(map(eval, segment.split("->")))
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            if x1 - x2 == 0:
                dx, dy = 0, (y2 - y1) // abs(y2 - y1)
            else:
                dx, dy = (x2 - x1) // abs(x2 - x1), 0

            xt, yt = x1, y1
            insert_board(xt, yt)
            while (not xt == x2) or (not yt == y2):
                xt += dx
                yt += dy
                insert_board(xt, yt)
    # line done


def add_sand():
    sx, sy = xsource, 0
    while True:
        if sy + 1 >= len(board):
            return True
        elif board[sy + 1][sx] not in ["#", "o"]:
            sy += 1
        elif board[sy + 1][sx - 1] not in ["#", "o"]:
            sy += 1
            sx -= 1
        elif board[sy + 1][sx + 1] not in ["#", "o"]:
            sy += 1
            sx += 1
        else:
            break
    board[sy][sx] = "o"

    return False


def p1(data):
    global board
    prepare_board(get_lines(data))

    done = False
    i = -1
    while not done:
        i += 1
        done = add_sand()

    # for line in board:
    #     print("".join(line))
    return i


def p2(data):
    global board
    prepare_board(get_lines(data))

    board.append(["." for _ in range(xrowlength)])
    board.append(["#" for _ in range(xrowlength)])

    done = False
    i = 0
    while not done:
        i += 1
        add_sand()
        done = board[0][xsource] == "o"

    # for line in board:
    # print("".join(line))
    return i


if __name__ == "__main__":
    data = read_file(f"ins/14.in")
    # data = read_file(f"samples/14.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
