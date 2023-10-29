import sys

sys.path.extend([".", ".."])

from utils import *
from tqdm import tqdm

rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # -
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # +
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # _|
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # |
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # o
]
rock_idx = 0
jet_ints = []
jet_idx = 0
peak = 0
chamber = set()

states = {}  # state => (peak, num rocks)
cycle_found = False
last_state = None
num_rocks_limit = 0
store_peak = 0


def reset_globals():
    global rock_idx, jet_idx, peak, chamber, states, cycle_found, last_state, last_info, num_rocks_limit
    rock_idx = 0
    jet_idx = 0
    peak = 0
    chamber = set()
    states = {}
    cycle_found = False
    last_state = None
    num_rocks_limit = 0


def create_actions(jets):
    global jet_ints
    jet_ints = [-1 if jet == "<" else 1 for jet in jets]


def get_next_jet():
    global jet_ints, jet_idx
    jet_int = jet_ints[jet_idx]
    jet_idx = (jet_idx + 1) % len(jet_ints)
    return jet_int


def get_next_rock():
    global rock, rock_idx
    rock = rocks[rock_idx]
    rock_idx = (rock_idx + 1) % len(rocks)
    return rock


def create_chamber_limits(upper_limit):
    global chamber
    # bottom row
    for i in range(8):
        chamber.add((i, 0))
    # walls
    for i in range(upper_limit):
        chamber.add((0, i))
        chamber.add((8, i))
    return


def move_rock(x, y, dx, dy, rock):
    global chamber
    x2, y2 = x + dx, y + dy
    for rdx, rdy in rock:
        rx = x2 + rdx
        ry = y2 + rdy
        if (rx, ry) in chamber:
            return 0, 0
    return dx, dy


# final position
def fall(total_rocks, p1=True):
    global chamber, peak, states, cycle_found, last_state, num_rocks_limit, store_peak, rock_idx, jet_idx

    rock = get_next_rock()
    x = 3
    y = peak + 4

    falling = True
    while falling:
        # move with jet
        jet = get_next_jet()
        dx, dy = move_rock(x, y, jet, 0, rock)
        x += dx
        y += dy
        # move down
        dx, dy = move_rock(x, y, 0, -1, rock)
        if dy == 0:  # then landed
            break
        x += dx
        y += dy

    # all all rock positions to the chamber
    for rdx, rdy in rock:
        chamber.add((x + rdx, y + rdy))
        peak = max(peak, y + rdy)

    if not cycle_found and not p1:
        state = []
        for i in range(1, 8):
            state.append(max([c[1] for c in chamber if c[0] == i]))
        min_state = min(state)
        state = tuple([c - min_state for c in state] + [rock_idx, jet_idx])
        if state in states:
            print(state)
            cycle_found = True
            prev_total_rocks, prev_peak = states[state]
            last_state = state
            cycle_peak_gain = peak - prev_peak
            cycle_total_rocks = total_rocks - prev_total_rocks  # cycle len

            cycles_skipped = (num_rocks_limit - total_rocks) // cycle_total_rocks
            store_peak = cycle_peak_gain * cycles_skipped
            print(f"{cycle_total_rocks=}, {cycles_skipped=}")
            return cycles_skipped * cycle_total_rocks
        else:
            states[state] = (total_rocks, peak)
    return 1


def p1(data):
    global peak, num_rocks_limit
    num_rocks_limit = 2022
    jets = get_lines(data)[0]
    create_actions(jets)
    create_chamber_limits(100_000)
    for total_rocks in range(2022):
        fall(total_rocks)
    return peak


def p2(data):
    global peak, num_rocks_limit, store_peak
    jets = get_lines(data)[0]
    num_rocks_limit = 1_000_000_000_000

    create_actions(jets)
    create_chamber_limits(100_000)

    total_rocks = 0
    while total_rocks < num_rocks_limit:
        inc = fall(total_rocks + 1, p1=False)
        total_rocks += inc
        # print(f"iter: {total_rocks}, left: {num_rocks_limit - total_rocks}")
    return store_peak + peak - 1


if __name__ == "__main__":
    data = read_file(f"samples/17.in")
    data = read_file(f"ins/17.in")

    print(f"part 1: {p1(data)}")
    reset_globals()
    p2_peak = p2(data)
    corr_peak = 1514285714288
    print(
        f"part 2: {p2_peak}, diff: {p2_peak - corr_peak} correct: {p2_peak == corr_peak}"
    )
