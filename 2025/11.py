from collections import defaultdict, deque

from utils.parsing import get_lines, read_file


def parse(lines: list[str]) -> dict[str, list[str]]:
    G = defaultdict(list)
    for line in lines:
        a, neighs = line.split(": ")
        for n in neighs.split():
            G[a].append(n)
    return dict(G)


def bfs(G: dict[str, list[str]], start: str, end: str) -> int:
    count = 0
    q = deque([start])
    while len(q) > 0:
        n = q.popleft()
        if n == end:
            count += 1
            continue
        for neigh in G.get(n, []):
            q.append(neigh)
    return count


def dfs(G: dict[str, list[str]], node: str, end: str, state: int, dp: dict[tuple[str, int]]) -> int:
    ns = (node, state)
    if ns in dp:
        return dp[ns]

    if node == end:
        dp[ns] = 1 if state == 3 else 0  # when state is 3 both 'fft' and 'dac' has been found
        return dp[ns]

    ans = 0
    for neigh in G[node]:
        n_state = state
        if neigh == "fft":
            n_state |= 1
        if neigh == "dac":
            n_state |= 2
        ans += dfs(G, neigh, end, n_state, dp)

    dp[ns] = ans
    return ans


def p1(data: str) -> int:
    lines = get_lines(data)
    G = parse(lines)
    return bfs(G, "you", "out")


def p2(data: str) -> int:
    lines = get_lines(data)
    G = parse(lines)
    return dfs(G, "svr", "out", 0, {})


if __name__ == "__main__":
    data = read_file("2025/samples/11_1.in")
    data = read_file("2025/samples/11_2.in")
    data = read_file("2025/ins/11.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
