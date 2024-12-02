def get_lines(data):
    return data.strip("\n").split("\n")


def get_ints(data):
    data = data.strip("\n")
    return [int(d) for d in data.split()]


def get_int_lines(data):
    return [get_ints(d) for d in get_lines(data)]


def get_chunks(data):
    css = [d.split("\n") for d in data.strip("\n").split("\n\n")]
    return [[c.strip() for c in cs] for cs in css]


def get_int_chunks(data):
    data = data.strip("\n")
    return [[int(c) for c in d.split()] for d in data.split("\n\n")]


def read_file(fp, mode="r"):
    return open(fp, mode).read().strip("\n")
