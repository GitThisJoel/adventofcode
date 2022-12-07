import sys

sys.path.extend([".", ".."])

from utils import *

dir_sizes = dict()
fs = dict()  # dir: [(type/size, name)]


def calc_dir_sizes(dn):
    global dir_sizes
    global fs
    s = 0
    for t, n in fs[dn]:
        if t == "dir":
            rn = dn + "_" + n
            if rn not in dir_sizes:
                calc_dir_sizes(rn)
            s += dir_sizes[rn]
        else:
            s += t
    dir_sizes[dn] = s
    return


def read_data(data):
    global dir_sizes
    global fs

    lines = get_lines(data)
    ds = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if line[0] == "$":
            cmd = line.split()[1:]  # remove $
            if len(cmd) == 2:  # cd
                _, dn = cmd
                if dn == "..":
                    # print(ds, dn)
                    ds.pop(-1)
                elif dn == "/":  # in ds:
                    # ind = ds.index(dn)
                    # ds = ds[: ind + 1]
                    ds = ["/"]
                else:
                    ds.append(dn)
                # else "ls", just cont.
                # print("read", cmd, "\t", ds)
        else:
            t, n = line.split()
            if t != "dir":
                t = int(t)

            d = "_".join(ds)
            # if d == "zsmhsbp":
            #     print(d, t, n)
            if d in fs:
                fs[d].add((t, n))
            else:
                fs[d] = {(t, n)}
            # print(fs[d])

    # for f, dn in fs.items():
    #     print(f, "\t", [n for d, n in dn if d == "dir"])

    calc_dir_sizes("/")  # calc all sizes
    return


def p1(data):
    global dir_sizes
    global fs

    read_data(data)

    t = 0
    for _, s in dir_sizes.items():
        if s <= 100000:
            t += s
    return t


def p2(data):
    global dir_sizes
    global fs

    read_data(data)

    tot = dir_sizes["/"]
    unused = 70000000 - tot
    diff = 30000000 - unused
    s_sizes = {
        key: val
        for key, val in sorted(dir_sizes.items(), key=lambda lam: lam[1], reverse=True)
    }

    print("tot =", tot)
    print("diff\n" + str(diff))

    prev = 0
    for _, v in s_sizes.items():
        print(v)
        if v - diff < 0:
            print("here")
            return prev
        prev = v


if __name__ == "__main__":
    data = read_file(f"ins/07.in")
    # data = read_file(f"samples/07.in")

    # print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
