import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *

type_idx = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}
DP = {}


def read_blueprints(lines):
    blueprints = []
    for line in lines:
        blueprint = [[] for _ in range(4)]
        robots = line.split(": ")[1]
        for robot in robots.split(".")[:-1]:
            c = [0, 0, 0, 0]
            robot_type, costs = robot.split(" costs ")
            robot_type = robot_type.split()[1]
            costs = costs.split(" and ")
            costs = [c.split() for c in costs]
            for amount, resource in costs:
                c[type_idx[resource]] = int(amount)
            blueprint[type_idx[robot_type]] = tuple(c[:-1])
        blueprints.append(blueprint)
    return blueprints


def add(left, right):
    return list(l + r for l, r in zip(left, right))


def sub(left, right):
    return list(l - r for l, r in zip(left, right))


def max_geodes(blueprint, n_ore, n_clay, n_obsidian, r_ore, r_clay, r_obsidian, r_geode, time_left):
    global DP

    if time_left == 0:
        return 0

    state = (n_ore, n_clay, n_obsidian, r_ore, r_clay, r_obsidian, r_geode, time_left)
    if state in DP:
        return DP[state]

    best = 0
    ns = n_ore, n_clay, n_obsidian
    rs = r_ore, r_clay, r_obsidian, r_geode

    available = [min(sub(ns, bp)) >= 0 for bp in blueprint]
    for j, avail in enumerate(available[::-1]):
        if not avail:
            continue
        i = len(available) - 1 - j  # rev

        # resources: rm cost for robot at blueprint[i]
        ns2 = sub(ns, blueprint[i])
        assert min(ns2) >= 0

        # robots: add a robot i
        one = [0, 0, 0, 0]
        one[i] = 1
        r_ore2, r_clay2, r_obsidian2, r_geode2 = add(rs, one)

        # resources: add production of robots
        #   (recall, new robot have not yet been built)
        n_ore2, n_clay2, n_obsidian2 = add(ns2, rs)

        mg = max_geodes(blueprint, n_ore2, n_clay2, n_obsidian2, r_ore2, r_clay2, r_obsidian2, r_geode2, time_left - 1)
        best = max(best, r_geode + mg)
        if i >= 2:
            DP[state] = best
            return best

    n_ore2, n_clay2, n_obsidian2 = add(ns, rs)
    best = max(
        best,
        r_geode
        + max_geodes(blueprint, n_ore2, n_clay2, n_obsidian2, r_ore, r_clay, r_obsidian, r_geode, time_left - 1),
    )
    DP[state] = best

    return best


def p1(data):
    global DP

    lines = get_lines(data)
    blueprints = read_blueprints(lines)
    pprint(blueprints)

    tl = 24
    tot_quality_level = 0
    for i, blueprint in enumerate(blueprints, 1):
        DP = {}
        num_geodes = max_geodes(blueprint, 0, 0, 0, 1, 0, 0, 0, tl)
        print(f"blueprint {i}: {num_geodes}")
        tot_quality_level += num_geodes * i
    return tot_quality_level


def p2(data):
    global DP

    lines = get_lines(data)
    blueprints = read_blueprints(lines)
    blueprints = blueprints[:3]
    pprint(blueprints)

    tl = 32
    mul_score = 1
    for i, blueprint in enumerate(blueprints, 1):
        DP = {}
        num_geodes = max_geodes(blueprint, 0, 0, 0, 1, 0, 0, 0, tl)
        print(f"blueprint {i}: {num_geodes}")
        mul_score *= num_geodes
    return mul_score


if __name__ == "__main__":
    data = read_file(f"samples/19.in")
    data = read_file(f"ins/19.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
