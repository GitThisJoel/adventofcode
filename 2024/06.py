import sys

sys.path.extend([".", ".."])

from utils import *

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # dx,dy


def get_start(B) -> tuple[int, int]:
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == "^":
                return (i, j)
    return len(B), len(B[0])  # impossible state


def path(B, replacement=None) -> tuple[set, bool]:
    d = 0
    y, x = get_start(B)
    dx, dy = dirs[d]
    vis = set()

    while True:
        if (y, x, dx, dy) in vis:  # loop detected
            return vis, True
        vis.add((y, x, dx, dy))

        if not ((0 <= (x + dx) < len(B[0])) and (0 <= (y + dy) < len(B))):  # steps outside of board, no loops
            return vis, False

        if B[y + dy][x + dx] == "#" or (y + dy, x + dx) == replacement:  # turn
            d = (d + 1) % len(dirs)
            dx, dy = dirs[d]
            # This 'continue' is very important!
            #  A position can have multiple directions, i.e. in corners.
            #  If we do not have 'continue' here we would have stepped to the next position and skipped the
            #   state where poistion is the same but it is pointing in a new direction, so: add both
            #   (pos, dir1) and (pos, dir2) to visited (dir1 != dir2).
            continue

        # step
        x += dx
        y += dy


def p1(data) -> int:
    B = get_lines(data)
    path_elements, _ = path(B)
    return len(set((a, b) for a, b, _, _ in path_elements))  # only interested in unique positions


def p2(data) -> int:
    B = get_lines(data)
    path_elements, _ = path(B)
    pot_pos = set((a, b) for a, b, _, _ in path_elements)

    ans = 0
    for y, x in pot_pos:
        _, loop = path(B, (y, x))
        ans += 1 if loop else 0
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/06.in")
    data = read_file(f"2024/ins/06.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
