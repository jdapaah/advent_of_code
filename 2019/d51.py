shift = {1: 4, 2: 4, 3: 2, 4: 2}
inp = 1


def main():
    with open('/Users/jeremy/AdventOfCode/Input/d5.txt') as file:
        program = [int(num) for num in file.readline().split(',')]
    pointer = 0

    opcode = program[pointer]
    while opcode != 99:
        full_opcode = opcode
        opcode %= 100
        if opcode == 1:
            num1, num2, to_addr = opcode12(full_opcode, program, pointer)
            program[to_addr] = num1 + num2
        elif opcode == 2:
            num1, num2, to_addr = opcode12(full_opcode, program, pointer)
            program[to_addr] = num1 * num2
        elif opcode == 3:  # will always be an writer, no imm option
            to_addr = program[pointer + 1]
            program[to_addr] = inp
        elif opcode == 4:
            num1 = opcode4(full_opcode, program, pointer)
            print('Exit code:', pointer, num1)
        else:
            print('Something is wrong, bad opcode')
            print(full_opcode)
            exit(1)

        pointer += shift[opcode % 100]
        opcode = program[pointer]


def opcode12(oc, prog, point):
    oc = str(oc)  # full opcode with parameter modes
    while len(oc) != 5:  # set up to number of inputs, not just 5
        oc = '0' + oc  # add leading zeros
    par_modes = oc[2:0:-1]  # splice parameter modes for inputs

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
    # to_addr is a writer, will always be pos
    return num1, num2, prog[point + 3]


def opcode4(oc, prog, point):
    if oc // 100 == 0:  # always one element
        addr1 = prog[point + 1]
        num1 = prog[addr1]
    else:
        num1 = prog[point + 1]
    return num1


if __name__ == '__main__':
    main()