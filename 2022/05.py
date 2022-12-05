import sys

sys.path.extend([".", ".."])

from utils import *

from queue import LifoQueue


def p1(data):
    chunks = [d.split("\n") for d in data.split("\n\n")]
    stacks = [LifoQueue() for _ in range(len(chunks[0][-1].split()))]

    # stacks
    for line in chunks[0][:-1][::-1]:
        for i in range(len(stacks)):
            crate = line[4 * i : 4 * i + 3].strip()
            if len(crate) == 3:
                stacks[i].put(crate[1])

    # instructions
    for line in chunks[1]:
        # move 1 from 1 to 2
        a, b, c = list(map(int, line.split()[1::2]))
        for _ in range(a):
            stacks[c - 1].put(stacks[b - 1].get())

    return "".join(s.get() for s in stacks)


def p2(data):
    chunks = [d.split("\n") for d in data.split("\n\n")]
    stacks = [list() for _ in range(len(chunks[0][-1].split()))]

    # stacks
    for line in chunks[0][:-1]:
        for i in range(len(stacks)):
            crate = line[4 * i : 4 * i + 3].strip()
            if len(crate) == 3:
                stacks[i].append(crate[1])

    # instructions
    for line in chunks[1]:
        # move 1 from 1 to 2
        a, b, c = list(map(int, line.split()[1::2]))
        stacks[c - 1] = stacks[b - 1][:a] + stacks[c - 1]
        stacks[b - 1] = stacks[b - 1][a:]
    return "".join(s[0] for s in stacks)


if __name__ == "__main__":
    data = read_file(f"ins/05.in")
    # data = read_file(f"samples/05.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
