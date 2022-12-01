def get_lines(data):
    return data.strip("\n").split("\n")


def get_ints(data):
    data = data.strip("\n")
    return [int(d) for d in data.split()]


def get_chunks(data):
    return [d.split("\n") for d in data.strip("\n").split("\n\n")]


def get_int_chunks(data):
    data = data.strip("\n")
    return [[int(c) for c in d.split()] for d in data.split("\n\n")]

def read_file(fp, mode="r"):
    return open(fp, mode).read().strip("\n")