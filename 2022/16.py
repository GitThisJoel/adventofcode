import sys

sys.path.extend([".", ".."])

from utils import *

import parse
from collections import deque
from pprint import pprint

global valve2neigbour, flow_rates, valve_id, dists, DP
DP = {}


def parse_input(inp):
    frmt = "Valve {valve_name} has flow rate={flow_rate:d}; "
    if "tunnels" in inp:
        frmt += "tunnels lead to valves {neighbours}"
    else:
        frmt += "tunnel leads to valve {neighbours}"
    values = parse.parse(frmt, inp).named
    values["neighbours"] = [v.strip() for v in values["neighbours"].split(",")]
    return values


def build_graphs(parsed_lines):
    global valve2neigbour, flow_rates, valve_id, dists

    valve2neigbour, flow_rates, valve_id = {}, {}, {}
    for parsed_line in parsed_lines:
        valve_name = parsed_line["valve_name"]
        flow_rate = parsed_line["flow_rate"]
        neighbours = parsed_line["neighbours"]
        valve2neigbour[valve_name] = neighbours
        flow_rates[valve_name] = flow_rate
    i = 0
    for vn, r in flow_rates.items():
        if r == 0:
            continue
        valve_id[vn] = i
        i += 1
    return valve2neigbour, flow_rates, valve_id


def distance_to_all_other():
    global valve2neigbour, flow_rates, valve_id, dists

    dists = dict()
    for valve in valve2neigbour:
        if valve != "AA" and flow_rates[valve] == 0:
            continue

        dists[valve] = {valve: 0, "AA": 0}
        visited = {valve}
        q = deque([(valve, 0)])

        while q:
            temp_val, dist = q.popleft()
            for neighbour in valve2neigbour[temp_val]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                if flow_rates[neighbour] > 0:
                    dists[valve][neighbour] = dist + 1
                q.append((neighbour, dist + 1))

        del dists[valve][valve]
        if valve != "AA":
            del dists[valve]["AA"]

    return dists


def optimize(valve: str, time_left: int, bitmask: int):
    global valve2neigbour, flow_rates, valve_id, dists, DP

    if (valve, time_left, bitmask) in DP:
        return DP[(valve, time_left, bitmask)]

    max_release = 0
    for neighbour in dists[valve]:
        bit = 1 << valve_id[neighbour]
        if bitmask & bit:
            continue

        tl = time_left - dists[valve][neighbour] - 1
        if time_left <= 0:
            continue

        curr_release = flow_rates[neighbour] * tl
        max_release = max(
            max_release,
            curr_release + optimize(neighbour, tl, bitmask | bit),
        )
    DP[(valve, time_left, bitmask)] = max_release
    return max_release


def name_pprint(name, value):
    print(f"{name}=")
    pprint(value)
    print()


def debug_prints():
    global valve2neigbour, flow_rates, valve_id, dists
    name_pprint("flow_rates", flow_rates)
    name_pprint("valve_id", valve_id)
    name_pprint("dists", dists)
    name_pprint("valve2neigbour", valve2neigbour)


def create_graphs(data):
    lines = get_lines(data)
    parsed_lines = [parse_input(line) for line in lines]
    build_graphs(parsed_lines)
    distance_to_all_other()
    return


def p1(data):
    global valve2neigbour, flow_rates, valve_id, dists
    create_graphs(data)

    time_left = 30
    max_release = optimize("AA", time_left, 0)
    return max_release


def p2(data):
    global valve2neigbour, flow_rates, valve_id, dists
    create_graphs(data)

    time_left = 26
    max_v = (1 << len(valve_id)) - 1
    mr = 0
    for i in range((max_v + 1) // 2):
        mr = max(
            mr, optimize("AA", time_left, i) + optimize("AA", time_left, i ^ max_v)
        )

    return mr


if __name__ == "__main__":
    data = read_file(f"ins/16.in")
    # data = read_file(f"samples/16.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
