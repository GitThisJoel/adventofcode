import sys


sys.path.extend([".", ".."])

from pprint import pprint
from scanf import scanf
from types import SimpleNamespace
from tqdm import tqdm

from utils import *


def read_input(register_lines, program_str):
    registers = {}
    for line in register_lines:
        reg, val = scanf("Register %s: %d", line)
        registers[reg] = val
    program = list(map(int, program_str.strip().split(": ")[1].split(",")))
    return SimpleNamespace(**registers), program


def combo(operand, registers):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers.A
    elif operand == 5:
        return registers.B
    elif operand == 6:
        return registers.C
    raise Exception(f"OPERAND NOT SUPPORTED --> {operand}")


def run_program(registers, program):
    output = []
    ip = 0
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip_add = 2
        if opcode == 0:
            registers.A = int(registers.A / 2 ** combo(operand, registers))
        elif opcode == 1:
            registers.B = registers.B ^ operand
        elif opcode == 2:
            registers.B = combo(operand, registers) % 8
        elif opcode == 3:
            if registers.A != 0:
                ip = operand
                ip_add = 0
        elif opcode == 4:
            registers.B = registers.B ^ registers.C
        elif opcode == 5:
            val = combo(operand, registers) % 8
            output.append(val)
        elif opcode == 6:
            registers.B = int(registers.A / 2 ** combo(operand, registers))
        elif opcode == 7:
            registers.C = int(registers.A / 2 ** combo(operand, registers))
        ip += ip_add
    return output


def p1(data):
    register_lines, (program_str,) = get_chunks(data)
    registers, program = read_input(register_lines, program_str)
    output = run_program(registers, program)
    return ",".join(map(str, output))


def p2(data):
    register_lines, (program_str,) = get_chunks(data)
    registers, program = read_input(register_lines, program_str)

    candidates = {0}
    for i in range(len(program) - 1, -1, -1):
        tail = program[i:]
        new_candidates = set()
        for A in candidates:
            for delta in range(8):
                new_A = A * 8 + delta
                registers = SimpleNamespace(A=new_A, B=0, C=0)
                output = run_program(registers, program)
                if tail != output:
                    continue
                new_candidates.add(new_A)
        candidates = new_candidates

    registers = SimpleNamespace(A=min(candidates), B=0, C=0)
    output = run_program(registers, program)
    if output != program:
        print(f"{output=} != {program=}")
    return min(candidates)


if __name__ == "__main__":
    data = read_file(f"2024/samples/17.in")
    data = read_file(f"2024/ins/17.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
