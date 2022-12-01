import sys


def p1():
    s = 0
    m = -1
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            if s > m:
                m = s
            s = 0
        else:
            s += int(line)
    print(m)
    return


def p2():
    c = []
    s = 0
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            c.append(s)
            s = 0
        else:
            s += int(line)
    print(sum(sorted(c, reverse=True)[:3]))
    return


# print(f"part 1: ", end="")
# p1()
print(f"part 2: ", end="")
p2()
