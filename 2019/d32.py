from math import inf


def main():
    with open('/Users/jeremy/AdventOfCode/Input/d3.txt') as file:
        line1 = file.readline().split(',')
        for ind, instr in enumerate(line1):
            line1[ind] = instr[0], int(instr[1:])

        line2 = file.readline().split(',')
        for ind, instr in enumerate(line2):
            line2[ind] = instr[0], int(instr[1:])

    list_1 = list(enumerate(build_sets(line1)))  # keeps track of step number
    list_2 = list(enumerate(build_sets(line2)))
    con_set = {i[1] for i in list_1} & {j[1] for j in list_2}  # just the single tuple

    min_dist = inf
    # slower
    # for coord in con_set:
    #     temp = 0
    #     for i in list_1:
    #         if coord == i[1]:
    #             temp = i[0]
    #             break
    #     for i in list_2:
    #         if coord == i[1]:
    #             temp += i[0]
    #             break
    #     min_dist = min(min_dist, temp + 2)

    # faster
    cross_1 = [i for i in list_1 if i[1] in con_set]
    cross_2 = [j for j in list_2 if j[1] in con_set]

    cross_1 = sorted(cross_1, key=lambda tup: tup[1])
    cross_2 = sorted(cross_2, key=lambda tup: tup[1])

    for i in range(len(con_set)):
        min_dist = min(min_dist, cross_1[i][0] + cross_2[i][0] + 2)

    print(min_dist)


def build_sets(coords):  # build sets of all the points a wire contact
    large = list()
    x = 0
    y = 0
    for d, num in coords:
        if d == 'L':
            for i in range(x, x - num, -1):
                large.append((i - 1, y))
            x -= num
        elif d == 'R':
            for i in range(x, x + num):
                large.append((i + 1, y))
            x += num
        elif d == 'D':
            for j in range(y, y - num, -1):
                large.append((x, j - 1))
            y -= num
        else:  # elif d == 'U'
            for j in range(y, y + num):
                large.append((x, j + 1))
            y += num
    return large


if __name__ == '__main__':
    main()
