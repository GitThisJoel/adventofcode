import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
move_dir = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
R, C = -1, -1


def parse(B):
    global R, C
    R, C = len(B), len(B[0])
    walls = set()
    boxes = set()
    robot = ()
    for i in range(R):
        for j in range(C):
            c = B[i][j]
            if c == "@":
                robot = (i, j)
            elif c == "#":
                walls.add((i, j))
            elif c == "O":
                boxes.add((i, j))
    return walls, boxes, robot


def parse_double(B):
    global R, C
    R, C = len(B), len(B[0])
    walls = set()
    left_boxes = set()
    right_boxes = set()
    robot = ()
    for i in range(R):
        for j in range(C):
            c = B[i][j]
            i2 = 1 * i
            j2 = 2 * j
            if c == "@":
                robot = (i2, j2)
            elif c == "#":
                walls.add((i2, j2))
                walls.add((i2, j2 + 1))
            elif c == "O":
                left_boxes.add((i2, j2))
                right_boxes.add((i2, j2 + 1))
    C = C * 2
    return walls, robot, left_boxes, right_boxes


def create_board(small_B):
    R, C = len(small_B), len(small_B[0])
    B = [["." for _ in range(C * 2)] for _ in range(R)]
    robot = ()
    for i in range(R):
        for j in range(C):
            if small_B[i][j] == "#":
                B[i][2 * j] = "#"
                B[i][2 * j + 1] = "#"
            elif small_B[i][j] == "O":
                B[i][2 * j] = "["
                B[i][2 * j + 1] = "]"
            elif small_B[i][j] == "@":
                robot = i, 2 * j
                B[i][2 * j] = "@"
            else:
                B[i][2 * j] = "."
                B[i][2 * j + 1] = "."
    return B, robot


def print_board(walls, boxes, robot):
    B = [["." for _ in range(C)] for _ in range(R)]
    for i, j in walls:
        B[i][j] = "#"
    for i, j in boxes:
        B[i][j] = "O"
    i, j = robot
    B[i][j] = "@"
    print("\n".join(["".join(row) for row in B]))
    return


def print_board_double(B):
    print("\n".join("".join(lb) for lb in B))


def do_moves(walls, boxes, robot, moves):
    i, j = robot
    for move in moves:
        di, dj = move_dir[move]
        ni, nj = i + di, j + dj
        if (ni, nj) in walls:
            continue
        elif (ni, nj) in boxes:
            box_line = [(ni, nj)]
            while (ni + di, nj + dj) in boxes:
                box_line.append((ni + di, nj + dj))
                ni, nj = (ni + di, nj + dj)
            # ni,nj will be the first point outside of the boxes, in line with di,dj
            bi, bj = box_line[-1]
            bi, bj = bi + di, bj + dj
            if (bi, bj) in walls:
                continue
            # move all boxes
            boxes.remove(box_line[0])
            boxes.add((bi, bj))
            i, j = box_line[0]
        else:
            i, j = ni, nj
    return boxes


def calc_score(boxes):
    return sum(100 * i + j for i, j in boxes)


def move_h(B, robot, di, dj) -> tuple[int, int]:  # move dj: <-->
    assert di == 0, f"ERROR --> {di=}"

    i, j = nr = robot[0], robot[1] + dj
    to_move = [robot]
    while B[i][j] in "[]":
        to_move.append((i, j))
        i, j = i, j + dj
    if B[i][j] == "#":
        return robot
    for i, j in to_move[::-1]:
        B[i][j + dj] = B[i][j]
        B[i][j] = "."
    return nr


def move_v(B, robot, di, dj) -> tuple[int, int]:  # move di: ^v
    assert dj == 0, f"ERROR --> {dj=}"

    nr = robot[0] + di, robot[1]
    to_move = [robot]
    js = {robot[1]}
    i = robot[0] + di
    while True:
        if any(B[i][j] not in "[]." for j in js):
            break
        if all(B[i][j] == "." for j in js):
            break
        njs = set()
        for j in js:
            if B[i][j] == "[":
                njs.add(j + 1)
                njs.add(j)
                if (i, j) not in to_move:
                    to_move.append((i, j))
                if (i, j + 1) not in to_move:
                    to_move.append((i, j + 1))
            if B[i][j] == "]":
                njs.add(j - 1)
                njs.add(j)
                if (i, j) not in to_move:
                    to_move.append((i, j))
                if (i, j - 1) not in to_move:
                    to_move.append((i, j - 1))
        js = njs
        i += di
    if any(B[i][j] == "#" for j in js):
        return robot
    for i, j in to_move[::-1]:
        B[i + di][j] = B[i][j]
        B[i][j] = "."
    return nr


def p1(data):
    B, ml_moves = get_chunks(data)
    moves = "".join(m for m in ml_moves)
    walls, boxes, robot = parse(B)

    boxes = do_moves(walls, boxes, robot, moves)
    return calc_score(boxes)


def p2(data):
    small_B, ml_moves = get_chunks(data)
    moves = "".join(m for m in ml_moves)
    B, robot = create_board(small_B)

    for move in moves:
        di, dj = move_dir[move]
        if move in {"^", "v"}:
            robot = move_v(B, robot, di, dj)
        elif move in {"<", ">"}:
            robot = move_h(B, robot, di, dj)
        else:
            print(f"ERROR --> {move=}")

    ans = 0
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == "[":
                ans += 100 * i + j
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/15_1.in")
    data = read_file(f"2024/ins/15.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
