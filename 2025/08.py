from functools import reduce

from utils.parsing import get_lines, read_file


def dist(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    #  skip sqrt here since it doesn't affect the relative ordering
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def solve(data: str, early_stop: int = -1) -> tuple[dict[int, set[int]], int]:
    lines = get_lines(data)
    points = []
    for line in lines:
        points.append(tuple(map(int, line.split(","))))

    dists = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dists.append((i, j, dist(points[i], points[j])))
    dists.sort(key=lambda t: t[-1])

    # not optimal tbh
    groups = {i: {i} for i in range(len(points))}
    for c, (i, j, _) in enumerate(dists):
        if c == early_stop:
            break
        s = groups[i].union(groups[j])
        if len(points) == len(s):
            break
        for k in s:
            groups[k] = s
    return groups, points[i][0] * points[j][0]


def p1(data: str, n: int = 1000) -> int:
    groups, _ = solve(data, early_stop=n)
    vis = set()
    group_lens = []
    for g, group in groups.items():
        if g in vis:
            continue
        group_lens.append(len(group))
        vis = vis.union(group)
    group_lens.sort(reverse=True)
    return reduce(lambda a, b: a * b, group_lens[:3], 1)


def p2(data: str) -> int:
    _, xx = solve(data)
    return xx


if __name__ == "__main__":
    data = read_file("2025/samples/08.in")
    data = read_file("2025/ins/08.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
