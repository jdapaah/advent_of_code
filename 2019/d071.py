from itertools import permutations
from math import inf
shift = {1: 4, 2: 4,
         3: 2, 4: 2,
         5: 3, 6: 3,
         7: 4, 8: 4}


def main():
    with open('Input/d7.txt') as file:
        program = [int(num) for num in file.readline().split(',')]

    perm = permutations(range(5))
    output = -inf, (0,1,2,3,4)
    for p in list(perm):
        out_1 = run(program[:], p[0], 0)
        out_2 = run(program[:], p[1], out_1)
        out_3 = run(program[:], p[2], out_2)
        out_4 = run(program[:], p[3], out_3)
        out_5 = run(program[:], p[4], out_4), p
        output = max(output, out_5)
    print(output)


def run(program, phase, amp_input):
    pointer = 0
    opcode = program[pointer]
    first_input = True
    # print('b')
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
        elif opcode == 3 and first_input:  # save phase to index
            to_addr = program[pointer + 1]
            program[to_addr] = phase
            first_input = False
        elif opcode == 3 and not first_input:  # save amp input to index
            to_addr = program[pointer + 1]
            program[to_addr] = amp_input
        elif opcode == 4:  # print from index
            return harvest1(full_opcode, program, pointer)
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
        # print('a')


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
