from math import inf


def main():
    with open('Input/d15.txt') as file:
        program = [int(num) for num in file.readline().split(',')]
        print('Len of program', len(program))

    x, y = 0, 0
    grid = {(x, y): 3}
    p1 = Intcode()
    a = 'Not Done'
    while a != 'Complete':
        a = p1.out(program, grid, x, y)
        if type(a) == tuple:
            x, y = a


class Intcode:
    shift = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]

    def __init__(self):
        self.relative_base = 0
        self.pointer = 0

    def out(self, program, grid, x, y):
        full_opcode = program[self.pointer]
        last_dir = 1
        while full_opcode != 99:
            opcode = full_opcode % 100
            point_shift = False
            num2 = 0

            if opcode == 1:  # add
                num1, num2 = self.harvest2(full_opcode, program, self.pointer, self.relative_base)
                to_addr = program[self.pointer + 3] + (self.relative_base if len(str(full_opcode)) == 5 else 0)
                if len(program) <= to_addr:
                    program.extend([0] * (1 + to_addr - len(program)))
                program[to_addr] = num1 + num2
            elif opcode == 2:  # multiply
                num1, num2 = self.harvest2(full_opcode, program, self.pointer, self.relative_base)
                to_addr = program[self.pointer + 3] + (self.relative_base if len(str(full_opcode)) == 5 else 0)
                if len(program) <= to_addr:
                    program.extend([0] * (1 + to_addr - len(program)))
                program[to_addr] = num1 * num2
            elif opcode == 3:  # save to index
                to_addr = program[self.pointer + 1] + (self.relative_base if len(str(full_opcode)) == 3 else 0)
                if len(program) <= to_addr:
                    program.extend([0] * (1 + to_addr - len(program)))
                # d = ''
                # while not d.isdigit() or int(d) not in range(1, 5):
                #     d = inp
                # last_dir = int(d)
                inp = ''
                while inp == '' or inp not in list('wasd'):
                    inp = input('Input: ')
                last_dir = {'w': 1, 's': 2, 'a': 3, 'd': 4}[inp]

                program[to_addr] = last_dir
            elif opcode == 4:  # print from index
                num1 = self.harvest1(full_opcode, program, self.pointer, self.relative_base)
                tempx, tempy = [None, (x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)][last_dir]
                grid[(x, y)] = 1  # old droid pos
                if num1 == 0:
                    grid[(tempx, tempy)] = 0  # block found
                    grid[(x, y)] = 3  # droid did not move
                    printg(grid)
                else:
                    print('Now at', tempx, tempy)
                    if num1 == 2:
                        print('Oxygen found at', tempx, tempy)
                    grid[(tempx, tempy)] = 3  # move droid
                    self.pointer += 2
                    printg(grid)
                    return tempx, tempy
            elif opcode == 5:  # jump if true
                num1, num2 = self.harvest2(full_opcode, program, self.pointer, self.relative_base)
                point_shift = num1
            elif opcode == 6:  # jump if false
                num1, num2 = self.harvest2(full_opcode, program, self.pointer, self.relative_base)
                point_shift = not num1
            elif opcode == 7:  # less than
                num1, num2 = self.harvest2(full_opcode, program, self.pointer, self.relative_base)
                to_addr = program[self.pointer + 3] + (self.relative_base if len(str(full_opcode)) == 5 else 0)
                if len(program) <= to_addr:
                    program.extend([0] * (1 + to_addr - len(program)))
                program[to_addr] = int(num1 < num2)
            elif opcode == 8:  # equal to
                num1, num2 = self.harvest2(full_opcode, program, self.pointer, self.relative_base)
                to_addr = program[self.pointer + 3] + (self.relative_base if len(str(full_opcode)) == 5 else 0)
                if len(program) <= to_addr:
                    program.extend([0] * (1 + to_addr - len(program)))
                program[to_addr] = int(num1 == num2)
            elif opcode == 9:
                self.relative_base += self.harvest1(full_opcode, program, self.pointer, self.relative_base)
            else:
                print('Something is wrong, bad opcode')
                print(full_opcode)
                exit(1)
            self.pointer = num2 if point_shift else self.pointer + self.shift[opcode]
            full_opcode = program[self.pointer]
        print()
        return 'Complete'

    def harvest1(self, foc, prog, point, rb):
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

    def harvest2(self, foc, prog, point, rb):
        foc = str(foc)  # full opcode with parameter modes
        while len(foc) != 5:
            foc = '0' + foc  # add leading zeros
        par_modes = foc[2:0:-1]  # splice parameter modes for inputs foc[2], foc[1]

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

    def reset(self):
        self.relative_base = self.pointer = 0


def printg(grid):
    minx, maxx, miny, maxy = inf, -inf, inf, -inf

    for x, y in grid:  # get extremes
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)

    for y in range(maxy, miny - 1, -1):  # y from up to down
        for x in range(minx, maxx + 1):  # x from left to right
            print(['█', ' ', 'o', '\033[91m@', '~'][grid.get((x, y), 4)], end='\033[0m')
        print()
    print()


if __name__ == '__main__':
    main()
