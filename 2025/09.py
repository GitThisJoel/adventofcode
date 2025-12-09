from utils.parsing import get_lines, read_file


def area(pt1: tuple[int, int], pt2: tuple[int, int]) -> int:
    x1, y1 = pt1
    x2, y2 = pt2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def is_valid(pt_i: tuple[int, int], pt_j: tuple[int, int], points: list[tuple[int, int]]) -> bool:
    i1, j1 = points[pt_i]
    i2, j2 = points[pt_j]

    # point 1 is top left, point 2 is bottom right
    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    for i in range(len(points)):
        pi1, pj1 = points[i]
        pi2, pj2 = points[(i + 1) % len(points)]

        if pi1 == pi2:
            pj1, pj2 = min(pj1, pj2), max(pj1, pj2)
            if i1 < pi1 < i2 and (pj1 <= j1 < pj2 or pj1 < j2 <= pj2):
                return False
        elif pj1 == pj2:
            pi1, pi2 = min(pi1, pi2), max(pi1, pi2)
            if j1 < pj1 < j2 and (pi1 <= i1 < pi2 or pi1 < i2 <= pi2):
                return False
        else:
            raise Exception("Error!")
    return True


def p1(data: str) -> int:
    lines = get_lines(data)
    points: list[tuple[int, int]] = [tuple(map(int, line.split(","))) for line in lines]
    max_a = -1
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = area(points[i], points[j])
            max_a = max(max_a, d)
    return max_a


def p2(data: str) -> int:
    lines = get_lines(data)
    points: list[tuple[int, int]] = [tuple(map(int, line.split(","))) for line in lines]

    max_a = -1
    for i in range(len(points)):
        for j in range(len(points)):
            if is_valid(i, j, points):
                max_a = max(max_a, area(points[i], points[j]))
    return max_a


if __name__ == "__main__":
    data = read_file("2025/samples/09.in")
    data = read_file("2025/ins/09.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
