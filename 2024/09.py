import sys

sys.path.extend([".", ".."])

from utils import *


def print_state(N):  # debug function, prints state in a readable format
    s = ""
    for fid, n in N:
        if fid == -1:
            s += "." * n
            continue
        s += str(fid) * n
    print(s)


def p1(data):
    nums = [int(c) for c in data]
    N = []
    j = 0
    for i, n in enumerate(nums):
        e = [j if i % 2 == 0 else -1] * n
        if i % 2 == 0:
            j += 1
        N.extend(e)

    space_inds = [i for i, v in enumerate(N) if v == -1]
    for si in space_inds:
        while N[-1] == -1:
            N.pop()
        if si >= len(N):
            break
        N[si] = N.pop()

    return sum(i * v for i, v in enumerate(N))


def combine_spaces(N):
    SG = []
    g = []
    prev = N[0][0]
    for i, (fid, _) in enumerate(N[1:], start=1):
        if prev == fid == -1:
            g.append(i)
        else:
            if len(g) > 1:
                SG.append(g)
            g = [i]
        prev = fid

    if len(g) > 1:
        SG.append(g)

    for g in SG[::-1]:
        n = sum(N[i][1] for i in g)
        N = N[: min(g)] + [(-1, n)] + N[max(g) + 1 :]
    return N


def p2(data):
    nums = [int(c) for c in data]
    N = []  # list of (fid, len)
    j = 0
    for i, n in enumerate(nums):
        if i % 2 == 0:
            N.append((j, n))
            j += 1
        else:
            N.append((-1, n))

    while N[-1][0] == -1:
        N.pop()

    FID = N[-1][0]
    while FID > 0:
        while N[-1][0] == -1:
            N.pop()

        # find next file id
        fid, n, ind = -1, -1, -1
        for ind, (fid, n) in enumerate(N):
            if FID != fid:
                continue
            break

        # try to find a space that fits current file id
        for j in range(1, ind):  # first will always be a file
            if j >= ind:
                break
            ofid, on = N[j]
            if ofid != -1:
                continue
            if n <= on:
                N[ind] = (-1, n)
                N = N[:j] + [(fid, n), (ofid, on - n)] + N[j + 1 :]
                break
        N = combine_spaces(N)
        FID -= 1

    ans = 0
    j = 0
    for fid, n in N:
        if fid == -1:
            j += n
            continue
        for _ in range(n):
            ans += fid * j
            j += 1
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/09.in")
    data = read_file(f"2024/ins/09.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
