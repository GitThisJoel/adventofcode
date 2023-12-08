import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *
from collections import defaultdict

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_idx = {c: i for i, c in enumerate(cards)}
idx_card = {i: c for c, i in card_idx.items()}


def parse_lines(lines):
    card_counts = {}
    for line in lines:
        cards, bid = line.split()
        counts = defaultdict(lambda: 0)
        for c in cards:
            counts[c] += 1
        d = {"bid": int(bid), "counts": dict(counts)}
        card_counts[cards] = d
    return card_counts


# XXXXX = 0
# XXXX_ = 1
# XXXYY = 2
# XXX__ = 3
# XXYY_ = 4
# XX___ = 5
# _____ = 6
#
# Sorry for bad code :/
def find_type(counts, part2=False):
    ret: int
    values = list(counts.values())
    Js = counts.get("J", 0) if part2 else 0
    if 5 in values:
        # 0 or 5 Js
        ret = 0
    elif 4 in values:
        # 0-1,4 Js
        ret = 1 - Js if Js != 4 else 0
    elif 3 in values:
        # 0-3 Js
        if Js == 3:
            ret = 1
            if 2 in values:
                ret = 0
        elif 2 in values:
            # 0 or 2 Js
            assert Js in {0, 2}
            ret = 2 - Js
        else:
            # 0 or 1
            assert Js in {0, 1}
            ret = 3
            if Js > 0:
                ret -= Js + 1
    elif 2 in values:
        # 0-2 Js
        if values.count(2) == 2:
            ret = 4
            if Js == 1:
                ret = 2
            elif Js == 2:
                # pair of Js and pair of something else => 4 of something
                ret = 1
        else:
            ret = 5
            if Js > 0:
                ret = 3
    else:
        # 0 or 1 Js
        assert Js in {0, 1}
        ret = 6 - Js
    return ret


def hand_to_ints(hand):
    out = []
    for c in hand:
        out.append(card_idx[c])
    return out


def ints_to_hand(int_hand):
    out = ""
    for c in int_hand:
        out += idx_card[c]
    return out


def calc_ans(data, part2=False):
    lines = get_lines(data)
    card_counts = parse_lines(lines)

    type_hands = []
    for hand, values in card_counts.items():
        t = find_type(values["counts"], part2=part2)
        type_hands.append((t, hand_to_ints(hand)))

    type_hands.sort(reverse=True)
    ans = 0
    for i, int_hand in enumerate(type_hands):
        hand = ints_to_hand(int_hand[1])
        ans += (i + 1) * card_counts[hand]["bid"]

    return ans


def p1(data):
    return calc_ans(data)


def p2(data):
    global cards, card_idx, idx_card
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    card_idx = {c: i for i, c in enumerate(cards)}
    idx_card = {i: c for c, i in card_idx.items()}

    return calc_ans(data, part2=True)


if __name__ == "__main__":
    data = read_file(f"samples/07.in")
    data = read_file(f"ins/07.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
