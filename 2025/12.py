from utils.parsing import get_chunks, read_file


def p1(data: str) -> int:
    chunks = get_chunks(data)
    # shapes = []
    # for chunk in chunks[:-1]:
    #     shape = chunk[1:]
    #     curr = []
    #     for i in range(len(shape)):
    #         for j in range(len(shape)):
    #             if shape[i][j] != "#":
    #                 continue
    #             curr.append((i, j))
    #         shapes.append(curr)
    boards = []
    for line in chunks[-1]:
        shape, counts = line.split(": ")
        boards.append((tuple(map(int, shape.split("x"))), list(map(int, counts.split()))))

    ans = 0
    for (h, w), counts in boards:
        if (h // 3) * (w // 3) >= sum(counts):
            ans += 1
    return ans


def p2(data: str) -> str:
    return "Press the button :^)"


if __name__ == "__main__":
    data = read_file("2025/samples/12.in")
    data = read_file("2025/ins/12.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
