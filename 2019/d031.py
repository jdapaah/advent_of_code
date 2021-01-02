def main():
    with open('Input/d3.txt') as file:
        line1 = file.readline().split(',')
        for ind, instr in enumerate(line1):
            line1[ind] = instr[0], int(instr[1:])

        line2 = file.readline().split(',')
        for ind, instr in enumerate(line2):
            line2[ind] = instr[0], int(instr[1:])

    print(min([abs(x) + abs(y) for x, y in build_sets(line1) & build_sets(line2)]))


def build_sets(coords):  # build sets of all the points a wire contact
    large = set()
    x = 0
    y = 0
    for d, num in coords:
        if d == 'L':
            for i in range(x - 1, x - num - 1, -1):
                large.add((i, y))
            x -= num
        elif d == 'R':
            for i in range(x + 1, x + num + 1):
                large.add((i, y))
            x += num
        elif d == 'D':
            for j in range(y - 1, y - num - 1, -1):
                large.add((x, j))
            y -= num
        else:  # elif dls == 'U'
            for j in range(y + 1, y + num + 1):
                large.add((x, j))
            y += num
    return large


if __name__ == '__main__':
    main()
