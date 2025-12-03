from utils.parsing import get_single_digits_int_lines, read_file


def p1_init(data: str) -> int:
    # initial p1 approach
    lines = get_single_digits_int_lines(data)
    ans = 0
    for line in lines:
        left, prev_right, M = 0, -1, -1
        for right in range(1, len(line)):
            M = max(M, 10 * line[left] + line[right])
            if line[left] < line[right]:
                left = right
                prev_right = right + 1
            elif line[right] > line[prev_right]:
                prev_right = right
        ans += M
    return ans


def solve(data: str, n_digits: int) -> int:
    lines = get_single_digits_int_lines(data)
    ans = 0
    for line in lines:
        stack = []
        for i in range(len(line)):
            # remove all elements smaller than the line[i], unless the line is "depleted"
            while len(stack) > 0 and stack[-1] < line[i] and (len(stack) + len(line) - i - 1) >= n_digits:
                stack.pop()
            if len(stack) < n_digits:
                stack.append(line[i])
        ans += int("".join(str(v) for v in stack))
    return ans


def p1(data: str) -> int:
    return solve(data, 2)


def p2(data: str) -> int:
    return solve(data, 12)


if __name__ == "__main__":
    data = read_file("2025/samples/03.in")
    data = read_file("2025/ins/03.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
