def main():
    with open('Input/d15.txt') as file:
        program = [int(num) for num in file.readline().split(',')]

    p1 = Intcode()
    path = []
    x, y = p1.search(program, 0, 0, path, 0)
    print(path, len(path))
    print(x, y)
    fillup = p1.spread([(x, y, program)], [])
    print(fillup)


class Intcode:
    reverse = [0, 2, 1, 4, 3]

    def __init__(self):
        self.relative_base = 0
        self.pointer = 0

    @staticmethod
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

    @staticmethod
    def harvest2(foc, prog, point, rb):
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

    def out(self, program, inp):
        full_opcode = program[self.pointer]
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
                last_dir = inp  # auto run
                program[to_addr] = last_dir
            elif opcode == 4:  # print from index
                num1 = self.harvest1(full_opcode, program, self.pointer, self.relative_base)
                self.pointer += 2
                return num1
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
            self.pointer = num2 if point_shift else self.pointer + [0, 4, 4, 2, 2, 3, 3, 4, 4, 2][opcode]
            full_opcode = program[self.pointer]
        print()
        return 'Complete'

    def search(self, program, x, y, path, past_mov):
        for d in range(1, 5):
            if past_mov == self.reverse[d]:
                continue
            status_code = self.out(program, inp=d)
            if status_code:
                path.append(d)
                tempx, tempy = [None, (x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)][d]
                if status_code == 1:
                    potcoord = self.search(program, tempx, tempy, path, d)
                    if potcoord:
                        return potcoord
                    a = 'Backtracktime'  # in actuality, nothing happens with this line
                    # code continues to backtrack stage, where we destroy this step entirely
                else:
                    return tempx, tempy
        path.pop()  # scrap that movement
        d_to_go = self.reverse[past_mov]
        self.out(program, inp=d_to_go)  # will shift pointer back to correct
        # this is where the code returns None for the if potcoord

    def spread(self, newbies, checked):
        count = -1
        new_newbies = []
        while newbies:
            while newbies:
                x, y, program = newbies.pop()
                checked.append((x, y))
                for d in range(1, 5):
                    tempx, tempy = [None, (x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)][d]
                    new_pro = program.copy()
                    if (tempx, tempy) not in checked and self.out(new_pro, d):
                        new_newbies.append((tempx, tempy, new_pro))
            newbies = new_newbies.copy()
            new_newbies.clear()
            count += 1
        return count


if __name__ == '__main__':
    main()
