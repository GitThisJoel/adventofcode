from utils.grid_dirs import eight_dirs
from utils.parsing import get_lines, read_file


def is_valid(board, i, j) -> bool:
    if board[i][j] != "@":
        return False

    c = 0
    for di, dj in eight_dirs:
        if 0 <= i + di < len(board) and 0 <= j + dj < len(board[i]) and board[i + di][j + dj] == "@":
            c += 1
        if c >= 4:
            return False
    return True


def p1(data: str) -> int:
    board = get_lines(data)
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            ans += 1 if is_valid(board, i, j) else 0
    return ans


def p2(data: str) -> int:
    board = [[c for c in line] for line in get_lines(data)]  # need it mutable
    ans, count = 0, -1
    while count != 0:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if is_valid(board, i, j):
                    board[i][j] = "."
                    count += 1
        ans += count
    return ans


if __name__ == "__main__":
    data = read_file("2025/samples/04.in")
    data = read_file("2025/ins/04.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
