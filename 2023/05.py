import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def parse_chunks(chunks):
    seeds = list(map(int, chunks[0][0].strip().split(": ")[1].split()))
    maps = []
    for chunk in chunks[1:]:
        chunk_maps = []
        for line in chunk[1:]:
            chunk_maps.append(list(map(int, line.split())))
        maps.append(chunk_maps)
    return seeds, maps


def transform(seed, mmap):
    for dest_start, source_start, l in mmap:
        if source_start <= seed < source_start + l:
            return dest_start + seed - source_start
    return seed


def range_transform(L, D, mmap):
    """
    L = low
    H = high
    D = distance

    ds = destination start
    ss = source start
    se = source end
    l = range length

    cases:
    L  H  ss se || ss se L  H
    L  ss H  se
    ss L  H  se
    ss L  se H
    """

    H = L + D
    pseudo_left = L
    ret = []
    for ds, ss, l in mmap:
        se = ss + l
        diff = ds - ss
        if ss <= L < se or ss < H <= se:
            left = max(L, ss)
            right = min(H, se)
            ret.append((left + diff, right - left))  # se, l
            if left > pseudo_left:
                # add y = x
                ret.append((pseudo_left, left - pseudo_left))
            pseudo_left = right
    if pseudo_left < H:
        # add y = x
        ret.append((pseudo_left, H - pseudo_left))
    return ret


def p1(data):
    chunks = get_chunks(data)
    seeds, maps = parse_chunks(chunks)
    ans = 999999999999999999999
    for seed in seeds:
        for mmap in maps:
            seed = transform(seed, mmap)
        ans = min(ans, seed)
    return ans


def p2(data):
    chunks = get_chunks(data)
    seeds, maps = parse_chunks(chunks)
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    maps = [sorted(mmap, key=lambda t: t[1]) for mmap in maps]

    for mmap in maps:
        temp = []
        for seed in seeds:
            temp += range_transform(*seed, mmap)
        seeds = temp
    return min(seeds)[0]


if __name__ == "__main__":
    data = read_file(f"samples/05.in")
    data = read_file(f"ins/05.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
