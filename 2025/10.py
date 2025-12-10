from collections import deque

import numpy as np
import scipy

from utils.parsing import get_lines, read_file


def parse_line(line: str) -> tuple[str, list[tuple[int, ...]], tuple[int, ...]]:
    segments = line.split()
    diagram = segments[0][1:-1]
    buttons = [tuple(map(int, b[1:-1].split(","))) for b in segments[1:-1]]
    joltages = tuple(map(int, segments[-1][1:-1].split(",")))
    return diagram, buttons, joltages


def bfs(diagram: str, buttons: list[tuple[int, ...]]) -> int:
    target_state = {i for i in range(len(diagram)) if diagram[i] == "#"}
    q = deque()
    q.append((set(), 0))
    found = False
    while not found:
        state, t = q.popleft()
        for button in buttons:
            nstate = state.copy()
            for i in button:
                if i in nstate:
                    nstate.remove(i)
                else:
                    nstate.add(i)
            if len(target_state) == len(state) and target_state == state:
                return t
            q.append((nstate, t + 1))
    return -1


def p1(data: str) -> int:
    lines = get_lines(data)
    ans = 0
    # this is a pretty naive solution tbh
    for line in lines:
        diagram, buttons, _ = parse_line(line)
        ans += bfs(diagram, buttons)
    return ans


def using_mlip(buttons: list[tuple[int, ...]], joltages: tuple[int, ...]) -> int:
    presses = [1] * len(buttons)
    A = [[(1 if i in button else 0) for button in buttons] for i in range(len(joltages))]
    res = scipy.optimize.milp(
        c=presses,
        integrality=[1] * len(buttons),
        constraints=scipy.optimize.LinearConstraint(A=A, lb=np.array(joltages), ub=np.array(joltages)),
    )
    return round(res.fun)


def using_z3(buttons: list[tuple[int, ...]], joltages: tuple[int, ...]) -> int:
    from z3 import Int, Optimize

    # presses = [1] * len(buttons)
    presses = [Int(f"p_{i}") for i in range(len(buttons))]  # x
    A = [[(1 if i in button else 0) for button in buttons] for i in range(len(joltages))]
    Ax = [sum(A[i][j] * presses[j] for j in range(len(buttons))) for i in range(len(joltages))]

    opt = Optimize()
    for i in range(len(joltages)):
        t = joltages[i]
        opt.add(Ax[i] == t)
    for i in range(len(buttons)):
        opt.add(0 <= presses[i])

    opt.minimize(sum(presses))
    opt.check()
    m = opt.model()
    ans = sum(m[var].as_long() for var in presses)
    return ans


def p2(data: str) -> int:
    """
    L = len(joltages)
    N = len(buttons)
    // example
    buttons = [(0,3,4), (1,2), (0), ...]
    // max size = [N x L]

    c = [1,1,1, ... 1] // len == N, since only 1's => sum of x
    x = [p_1, p_2, ..., p_n] // number of presses per button
    A = [[(1 if i in button_n else 0) for n in range(N)] for i in range(L)]
    // example
    A^T = [[1,0,0,1,1], // but as columns instead as rows therefore A^T
           [0,1,1,0,0],
           [1,0,0,0,0],
           ...]

    Goal is to:
    minimize c @ x (sum)
    s.t. target <= Ax <= target
    (target == joltages)
    """

    lines = get_lines(data)
    ans_z3 = 0
    ans_milp = 0
    for line in lines:
        _, buttons, joltages = parse_line(line)
        ans_milp += using_mlip(buttons, joltages)
        ans_z3 += using_z3(buttons, joltages)
    assert ans_milp == ans_z3
    return ans_z3


if __name__ == "__main__":
    data = read_file("2025/samples/10.in")
    data = read_file("2025/ins/10.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
