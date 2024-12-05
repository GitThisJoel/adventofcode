import sys

sys.path.extend([".", ".."])

from utils import *


def parse(data):
    chunks = get_chunks(data)
    orders = []
    for order in chunks[0]:
        orders.append(tuple(map(int, order.strip().split("|"))))

    pages = []
    for p in chunks[1]:
        pages.append(tuple(map(int, p.strip().split(","))))

    return set(orders), pages


def check(page, orders):
    ok = True
    page = list(page)
    for i in range(len(page) - 1):
        for j in range(i + 1, len(page)):
            if (page[j], page[i]) in orders:
                page[i], page[j] = page[j], page[i]
                ok = False
    return ok, tuple(page)


def p1(data):
    orders, pages = parse(data)

    ans = 0
    for page in pages:
        ok, _ = check(page, orders)
        ans += page[len(page) // 2] if ok else 0
    return ans


def p2(data):
    orders, pages = parse(data)

    ans = 0
    for page in pages:
        ok, page = check(page, orders)
        ans += page[len(page) // 2] if not ok else 0
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/05.in")
    data = read_file(f"2024/ins/05.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
