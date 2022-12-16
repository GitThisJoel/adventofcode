import sys
from parse import parse

sys.path.extend([".", ".."])

from utils import *


# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3


def eval_op(s, old):
    return eval(s)


def load_data(data):
    chunks = get_chunks(data)
    # {x: {"items": [], "op": lambda, "test": y, "t": monkey m, "f": monkey n}}
    monkeys = {}
    monkey_items = []
    for chunk in chunks:
        (i,) = parse("Monkey {:d}:", chunk[0])
        (itms,) = parse("Starting items: {}", chunk[1])
        (op,) = parse("Operation: new = {}", chunk[2])
        (div,) = parse("Test: divisible by {:d}", chunk[3])
        (m,) = parse("If true: throw to monkey {:d}", chunk[4])
        (n,) = parse("If false: throw to monkey {:d}", chunk[5])

        itms = list(map(int, itms.split(",")))
        monkey_items.append(itms)

        monkeys[i] = {"op": op, "div": div, "t": m, "f": n}

    return monkeys, monkey_items


def p1(data):
    monkeys, monkey_items = load_data(data)

    rounds = 20
    num_monkeys = len(monkeys)

    num_inspected = [0] * num_monkeys
    for _ in range(rounds):
        for m in range(num_monkeys):
            for item in monkey_items[m]:
                l = eval_op(monkeys[m]["op"], item) // 3
                if l % monkeys[m]["div"] == 0:
                    monkey_items[monkeys[m]["t"]].append(l)
                else:
                    monkey_items[monkeys[m]["f"]].append(l)
                num_inspected[m] += 1
            monkey_items[m] = []
    x, y = sorted(num_inspected, reverse=True)[:2]
    return x * y


def p2(data):
    monkeys, monkey_items = load_data(data)

    rounds = 10_000
    num_monkeys = len(monkeys)

    num_inspected = [0] * num_monkeys

    mo = 1
    for x in [monkey["div"] for _, monkey in monkeys.items()]:
        mo *= x

    for _ in range(rounds):
        for m in range(num_monkeys):
            for item in monkey_items[m]:
                l = eval_op(monkeys[m]["op"], item)
                l = l % mo
                if l % monkeys[m]["div"] == 0:
                    monkey_items[monkeys[m]["t"]].append(l)
                else:
                    monkey_items[monkeys[m]["f"]].append(l)
                num_inspected[m] += 1
            monkey_items[m] = []
    x, y = sorted(num_inspected, reverse=True)[:2]
    print(num_inspected)
    return x * y


if __name__ == "__main__":
    data = read_file(f"ins/11.in")
    # data = read_file(f"samples/11.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
