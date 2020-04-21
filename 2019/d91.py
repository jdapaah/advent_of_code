shift = {1: 4, 2: 4,
         3: 2, 4: 2,
         5: 3, 6: 3,
         7: 4, 8: 4,
         9: 2}

inp = 2


def main():
    with open('/Users/jeremy/AdventOfCode/Input/d9.txt') as file:
        program = [int(num) for num in file.readline().split(',')] + [0] * 10000
    # print('length of program:', len(program))
    pointer = 0
    relative_base = 0
    full_opcode = program[pointer]
    while full_opcode != 99:
        # print(pointer, full_opcode, relative_base, end=', ')
        opcode = full_opcode % 100
        point_shift = False
        num2 = 0

        if opcode == 1:  # add
            num1, num2 = harvest2(full_opcode, program, pointer, relative_base)
            to_addr = program[pointer + 3] + (relative_base if len(str(full_opcode)) == 5 else 0)
            program[to_addr] = num1 + num2
        elif opcode == 2:  # multiply
            num1, num2 = harvest2(full_opcode, program, pointer, relative_base)
            to_addr = program[pointer + 3] + (relative_base if len(str(full_opcode)) == 5 else 0)
            program[to_addr] = num1 * num2
        elif opcode == 3:  # save to index
            to_addr = program[pointer + 1] + (relative_base if len(str(full_opcode)) == 3 else 0)
            program[to_addr] = inp
        elif opcode == 4:  # print from index
            num1 = harvest1(full_opcode, program, pointer, relative_base)
            print('[Exit code:%d]' % num1, end=' ')
            # print(num1, end=' ')
        elif opcode == 5:  # jump if true
            num1, num2 = harvest2(full_opcode, program, pointer, relative_base)
            point_shift = num1
            # print(program[1000], num1)
        elif opcode == 6:  # jump if false
            num1, num2 = harvest2(full_opcode, program, pointer, relative_base)
            point_shift = not num1
        elif opcode == 7:  # less than
            num1, num2 = harvest2(full_opcode, program, pointer, relative_base)
            to_addr = program[pointer + 3] + (relative_base if len(str(full_opcode)) == 5 else 0)
            program[to_addr] = int(num1 < num2)
        elif opcode == 8:  # equal to
            num1, num2 = harvest2(full_opcode, program, pointer, relative_base)
            to_addr = program[pointer + 3] + (relative_base if len(str(full_opcode)) == 5 else 0)
            program[to_addr] = int(num1 == num2)
        elif opcode == 9:
            relative_base += harvest1(full_opcode, program, pointer, relative_base)
        else:
            print('Something is wrong, bad opcode')
            print(full_opcode)
            exit(1)
        pointer = num2 if point_shift else pointer + shift[opcode]
        full_opcode = program[pointer]


def harvest2(oc, prog, point, rb):
    oc = str(oc)  # full opcode with parameter modes
    while len(oc) != 5:
        oc = '0' + oc  # add leading zeros
    par_modes = oc[2:0:-1]  # splice parameter modes for inputs

    if par_modes[0] == '0':
        addr1 = prog[point + 1]
        num1 = prog[addr1]
    elif par_modes[0] == '1':
        num1 = prog[point + 1]
    else:
        addr1 = rb + prog[point + 1]
        num1 = prog[addr1]

    if par_modes[1] == '0':
        addr2 = prog[point + 2]
        num2 = prog[addr2]
    elif par_modes[1] == '1':
        num2 = prog[point + 2]
    else:
        addr2 = rb + prog[point + 2]
        num2 = prog[addr2]

    return num1, num2


def harvest1(foc, prog, point, rb):
    par_mode = foc // 100
    if par_mode == 0:  # always one element
        addr1 = prog[point + 1]
        num1 = prog[addr1]
    elif par_mode == 1:
        num1 = prog[point + 1]
    else:
        addr1 = rb + prog[point + 1]
        num1 = prog[addr1]
    return num1


if __name__ == '__main__':
    main()
