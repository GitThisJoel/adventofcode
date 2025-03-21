import sys

sys.path.extend([".", ".."])

from itertools import permutations, product
from functools import cache
from pprint import pprint

from utils import *

inf = float("inf")

# key --> (i, j)
numpad = {
    "A": (3, 2),
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
}

# key --> (i, j)
keypad = {
    "A": (0, 2),
    "^": (0, 1),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

numpad_paths = {}
keypad_paths = {}


def create_paths():
    global numpad_paths, keypad_paths

    numpad_paths = {}
    for key1, (i1, j1) in numpad.items():
        for key2, (i2, j2) in numpad.items():
            if key1 == key2:
                keypad_paths[(key1, key2)] = ["A"]
                continue
            di, dj = i2 - i1, j2 - j1
            ver = "^" if di < 0 else "v"
            hor = "<" if dj < 0 else ">"
            moves = ver * abs(di) + hor * abs(dj)
            all_moves = list(set(map(lambda s: "".join(s), permutations(moves))))

            # cannot move over the blank space
            if j1 == 0 and i2 == 3:
                all_moves = list(filter(lambda s: not s.startswith("v" * (3 - i1)), all_moves))
            if i1 == 3 and j2 == 0:
                all_moves = list(filter(lambda s: not s.startswith("<" * j1), all_moves))
            numpad_paths[(key1, key2)] = [am + "A" for am in all_moves]

    keypad_paths = {}
    for key1, (i1, j1) in keypad.items():
        for key2, (i2, j2) in keypad.items():
            if key1 == key2:
                keypad_paths[(key1, key2)] = ["A"]
                continue
            di, dj = i2 - i1, j2 - j1
            ver = "^" if di < 0 else "v"
            hor = "<" if dj < 0 else ">"
            moves = ver * abs(di) + hor * abs(dj)
            all_moves = list(set(map(lambda s: "".join(s), permutations(moves))))

            # cannot move over the blank space
            if j1 == 0 and i2 == 0:
                all_moves = list(filter(lambda s: not s.startswith("^"), all_moves))
            if i1 == 0 and j2 == 0:
                all_moves = list(filter(lambda s: not s.startswith("<" * j1), all_moves))
            keypad_paths[(key1, key2)] = [am + "A" for am in all_moves]
    return numpad_paths, keypad_paths


def expand_numpad(code):
    global numpad_paths
    sub_paths = []
    for a, b in zip(code, code[1:]):
        sub_paths.append(numpad_paths[(a, b)])
    return sub_paths


@cache
def expand_keypad(start: str, moves: str, depth: int) -> tuple[str, int]:
    global keypad_paths

    if depth == 0:
        return len(moves)

    moves = start + moves
    best = 0
    for a, b in zip(moves, moves[1:]):
        paths = keypad_paths[(a, b)]
        min_len = inf
        for path in paths:
            l = expand_keypad("A", path, depth - 1)
            if min_len > l:
                min_len = l
        best += min_len
    return best


def complexity(l: int, code: str):
    return l * int(code.strip("A"))


def solve(data, depth):
    global numpad_paths, keypad_paths

    codes = get_lines(data)
    create_paths()

    ans = 0
    for code in codes:
        sub_paths = expand_numpad("A" + code)
        prods = list(map(lambda s: "".join(s), product(*sub_paths)))
        moves_len = inf
        for prod in prods:
            l = expand_keypad("A", prod, depth - 1)
            if moves_len > l:
                moves_len = l
        c = complexity(moves_len, code)
        ans += c
    return ans


def p1(data):
    return solve(data, 3)


def p2(data):
    return solve(data, 26)


if __name__ == "__main__":
    data = read_file(f"2024/samples/21.in")
    data = read_file(f"2024/ins/21.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
