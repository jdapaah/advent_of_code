from itertools import permutations
from math import inf

shift = {1: 4, 2: 4,
         3: 2, 4: 2,
         5: 3, 6: 3,
         7: 4, 8: 4}


def main():
    with open('/Users/jeremy/AdventOfCode/Input/d7.txt') as file:
        program = [int(num) for num in file.readline().split(',')]

    perm = permutations(range(5, 10))
    output = -inf, (0, 1, 2, 3, 4)

    for p in list(perm):
        point1, prog1 = 0, program[:]
        point2, prog2 = 0, program[:]
        point3, prog3 = 0, program[:]
        point4, prog4 = 0, program[:]
        point5, prog5 = 0, program[:]
        out_5 = 0
        while point5 is not None:
            out_1, prog1, point1 = run(prog1, p[0], out_5, point1)
            out_2, prog2, point2 = run(prog2, p[1], out_1, point2)
            out_3, prog3, point3 = run(prog3, p[2], out_2, point3)
            out_4, prog4, point4 = run(prog4, p[3], out_3, point4)
            out_5, prog5, point5 = run(prog5, p[4], out_4, point5)
        output = max(output, (out_5, p))
    print(output)


def run(program, phase, amp_input, init_p):
    pointer = init_p
    opcode = program[pointer]
    while opcode != 99:
        full_opcode = opcode
        opcode %= 100
        point_shift = False
        num2 = 0

        if opcode == 1:  # add
            num1, num2 = harvest2(full_opcode, program, pointer)
            to_addr = program[pointer + 3]
            program[to_addr] = num1 + num2
        elif opcode == 2:  # multiply
            num1, num2 = harvest2(full_opcode, program, pointer)
            to_addr = program[pointer + 3]
            program[to_addr] = num1 * num2
        elif opcode == 3:  # save input to index
            to_addr = program[pointer + 1]
            inp = phase if pointer == 0 else amp_input  # if at first input, chose phase else choose amp_input
            program[to_addr] = inp
        elif opcode == 4:  # print from index
            output = harvest1(full_opcode, program, pointer)
            return output, program, pointer + 2
        elif opcode == 5:  # jump if true
            num1, num2 = harvest2(full_opcode, program, pointer)
            point_shift = num1
        elif opcode == 6:  # jump if false
            num1, num2 = harvest2(full_opcode, program, pointer)
            point_shift = not num1
        elif opcode == 7:  # less than
            num1, num2 = harvest2(full_opcode, program, pointer)
            to_addr = program[pointer + 3]
            program[to_addr] = int(num1 < num2)
        elif opcode == 8:  # equal to
            num1, num2 = harvest2(full_opcode, program, pointer)
            to_addr = program[pointer + 3]
            program[to_addr] = int(num1 == num2)
        else:
            print('Something is wrong, bad opcode')
            print(full_opcode)
            exit(1)
        pointer = num2 if point_shift else pointer + shift[opcode]
        opcode = program[pointer]
    return amp_input, None, None  # hits 99, done running


def harvest2(oc, prog, point):
    oc = str(oc)  # full opcode with parameter modes
    while len(oc) != 4:
        oc = '0' + oc  # add leading zeros
    par_modes = oc[1::-1]  # splice parameter modes for inputs

    if par_modes[0] == '0':
        addr1 = prog[point + 1]
        num1 = prog[addr1]
    else:
        num1 = prog[point + 1]
    if par_modes[1] == '0':
        addr2 = prog[point + 2]
        num2 = prog[addr2]
    else:
        num2 = prog[point + 2]

    return num1, num2


def harvest1(oc, prog, point):
    if oc // 100 == 0:  # always one element
        addr1 = prog[point + 1]
        num1 = prog[addr1]
    else:
        num1 = prog[point + 1]
    return num1


if __name__ == '__main__':
    main()
