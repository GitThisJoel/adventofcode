import sys

sys.path.extend([".", ".."])

from collections import defaultdict
from pprint import pprint

from utils import *


def create_G(lines):
    G = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        G[a].add(b)
        G[b].add(a)
    return G


def bfs(G, node, path, paths: set, depth):
    if depth == 0:
        assert len(path) == 3
        # if last node has a edge back to first node
        if path[0] in G[path[-1]]:
            paths.add(tuple(sorted(path)))
        return paths

    ns = G[node]
    for n in ns:
        if n in path:
            continue
        p = path[:]  # copy path
        p.append(n)
        bfs(G, n, p, paths, depth - 1)

    return paths


def find_groups(G, depth=3):
    paths = set()
    for node in G.keys():
        bfs(G, node, [node], paths, depth - 1)
    return paths


def group_contain_t(group):
    ok = False
    for g in group:
        if g[0] == "t":
            ok = True
            break
    return ok


def find_biggest_group(G):
    biggest_group = []

    def dfs(G, node, path: list, visited: set):
        nonlocal biggest_group
        path.append(node)
        visited.add(node)

        # only let fully conected paths through
        if len(path) > len(biggest_group):
            biggest_group = path[:]

        for n in G[node]:
            if n in visited:
                continue
            if not all(p in G[n] for p in path):
                visited.add(n)
                continue
            dfs(G, n, path[:], visited)
        return

    for node in G.keys():
        dfs(G, node, [], set())
    return biggest_group


def p1(data):
    lines = get_lines(data)
    G = create_G(lines)
    groups = find_groups(G)

    l = list(filter(lambda g: group_contain_t(g), groups))
    return len(l)


def p2(data):
    lines = get_lines(data)
    G = create_G(lines)
    cycle = find_biggest_group(G)

    return ",".join(sorted(cycle))


if __name__ == "__main__":
    data = read_file(f"2024/samples/23.in")
    data = read_file(f"2024/ins/23.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
