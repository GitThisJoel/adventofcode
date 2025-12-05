from utils.parsing import get_chunks, read_file


def parse_ranges(lines: list[str]) -> list[tuple[int, int]]:
    rs = []
    for line in lines:
        t = tuple(map(int, line.strip().split("-")))
        rs.append(t)
    return rs


def is_fresh(i: int, ranges: list[tuple[int, int]]) -> bool:
    for l, r in ranges:
        if l <= i <= r:
            return True
    return False


def overlapping_ranges(range_1: tuple[int, int], range_2: tuple[int, int]) -> tuple:
    l1, r1 = range_1
    l2, r2 = range_2
    if max(l1, l2) <= min(r1, r2):
        return min(l1, l2), max(r1, r2)
    return ()


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = ranges[:]  # copy
    to_remove = {-1}
    while len(to_remove) != 0:
        to_remove = set()
        for i in range(len(merged)):
            for j in range(i + 1, len(merged)):
                if j in to_remove or i in to_remove:
                    continue
                t = overlapping_ranges(merged[i], merged[j])
                if len(t) > 0:
                    merged[i] = t
                    to_remove.add(j)
        for i in sorted(list(to_remove), reverse=True):
            merged.pop(i)
    return merged


def p1(data: str) -> int:
    chunks = get_chunks(data)
    ranges = parse_ranges(chunks[0])

    ans = 0
    for line in chunks[1]:
        if is_fresh(int(line), ranges):
            ans += 1
    return ans


def p2(data: str) -> int:
    chunks = get_chunks(data)
    ranges = parse_ranges(chunks[0])
    ans = 0
    for l, r in merge_ranges(ranges):
        ans += r - l + 1
    return ans


if __name__ == "__main__":
    data = read_file("2025/samples/05.in")
    data = read_file("2025/ins/05.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
