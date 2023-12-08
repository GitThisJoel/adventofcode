import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *
from collections import defaultdict, Counter


def parse_lines(lines):
    M = {}
    for line in lines:
        node, neighs = line.split(" = ")
        left, right = neighs.split(", ")
        assert node not in M
        M[node] = (left[1:], right[:-1])
    return M


def divisors(n):
    divs = []
    while n % 2 == 0:
        divs.append(2)
        n //= 2
    d = 3
    while n > 1:
        if d > n:
            break
        while n % d == 0:
            divs.append(d)
            n //= d
        d += 2
    return Counter(divs)


def p1(data):
    chunks = get_chunks(data)
    LR = chunks[0][0]
    M = parse_lines(chunks[1])

    curr = "AAA"
    steps = 0
    while curr != "ZZZ":
        inst = 0 if LR[steps % len(LR)] == "L" else 1
        curr = M[curr][inst]
        steps += 1
    return steps


def p2(data):
    chunks = get_chunks(data)
    LR = chunks[0][0]
    M = parse_lines(chunks[1])

    nodes = [node for node in M.keys() if node[-1] == "A"]
    cycles = []
    for node in nodes:
        Z = {}
        steps = 0
        curr = node
        found = False
        while not found:
            inst = 0 if LR[steps % len(LR)] == "L" else 1
            curr = M[curr][inst]
            steps += 1
            if curr[-1] == "Z":
                if curr in Z:
                    found = True
                else:
                    Z[curr] = steps
        cycles.append(Z[curr])

    divs = defaultdict(lambda: 0)
    for steps in cycles:
        ds = divisors(steps)
        for d, amount in ds.items():
            divs[d] = max(divs[d], amount)

    ans = 1
    for n, power in divs.items():
        ans *= n**power
    return ans


if __name__ == "__main__":
    data = read_file(f"samples/08.in")
    data = read_file(f"ins/08.in")
    print(f"part 1: {p1(data)}")

    data = read_file(f"samples/08_2.in")
    data = read_file(f"ins/08.in")
    print(f"part 2: {p2(data)}")
