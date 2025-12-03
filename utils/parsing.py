from pathlib import Path


def get_lines(data: str) -> list[str]:
    return data.strip("\n").split("\n")


def get_single_digits_ints(data: str) -> list[int]:
    return [int(d) for d in data.strip()]


def get_single_digits_int_lines(data: str) -> list[list[int]]:
    return [get_single_digits_ints(d) for d in get_lines(data)]


def get_ints(data: str) -> list[int]:
    data = data.strip("\n")
    return [int(d) for d in data.split()]


def get_int_lines(data: str) -> list[list[int]]:
    return [get_ints(d) for d in get_lines(data)]


def get_chunks(data: str) -> list[list]:
    css = [d.split("\n") for d in data.strip("\n").split("\n\n")]
    return [[c.strip() for c in cs] for cs in css]


def get_int_chunks(data: str) -> list[list[int]]:
    data = data.strip("\n")
    return [[int(c) for c in d.split()] for d in data.split("\n\n")]


def read_file(fp: str | Path) -> str:
    return open(fp, "r").read().strip("\n")
