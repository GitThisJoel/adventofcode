from utils.parsing import get_chunks, get_lines, read_file


def p1(data):
    lines = get_lines(data)
    chunks = get_chunks(data)

    ans = 0
    return 0


def p2(data):
    lines = get_lines(data)
    chunks = get_chunks(data)

    ans = 0
    return 0


if __name__ == "__main__":
    data = read_file("yyyy/ins/dddd.in")
    data = read_file("yyyy/samples/dddd.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
