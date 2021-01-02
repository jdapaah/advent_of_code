def main():
    best = (-1, (0, 0))
    count = 0
    with open('Input/d10.txt') as file:
        field = [line.strip() for line in file]
    for y, row in enumerate(field):  # dist from top
        for x, el in enumerate(row):  # dist from left
            if el == '#':
                count += 1
                best = max(best, visible(field, y, x))

    print('Number of total asteroids', count)
    print('Best line of sight is found at %s; we can see %d asteroids' % (best[1], best[0]))
    x, y = best[1]
    fl = ordered(field, x, y)
    print(len(fl))
    print(fl[0], fl[1], fl[2], fl[9], fl[19], fl[49], fl[99], fl[198], fl[199], fl[200], fl[298])
    print(fl[199])


def visible(field, i, j):  # edit to get the closest asteroid first
    slope_field = set()
    count = 0
    for tempy, row in enumerate(field):
        for tempx, el in enumerate(row):
            if tempy == i or tempx == j or el == '.':
                continue
            sign = (tempy - i) / abs(tempy - i)
            s = (tempx - j) / (tempy - i), sign
            if s not in slope_field:
                count += 1
                slope_field.add(s)

    for tempy in range(i - 1, -1, -1):
        if field[tempy][j] == '#':
            count += 1
            break
    for tempy in range(i + 1, len(field)):
        if field[tempy][j] == '#':
            count += 1
            break
    for tempx in range(j - 1, -1, -1):
        if field[i][tempx] == '#':
            count += 1
            break
    for tempx in range(j + 1, len(field[0])):
        if field[i][tempx] == '#':
            count += 1
            break

    return count, (j, i)  # j is x, i is y


def ordered(field, x, y):
    slope_dict = dict()

    for ty, row in enumerate(field):
        for tx, el in enumerate(row):
            if el == '.' or (tx == x and ty == y):
                continue
            elif tx == x and ty < y:  # top
                sign, slope = -1, -100000
            elif ty == y and tx > x:  # right
                sign, slope = -1, 0
            elif tx == x and ty > y:  #
                sign, slope = 1, -100000
            elif ty == y and tx < x:
                sign, slope = 1, 0
            else:
                sign = -(tx - x) / abs(tx - x)  # right half +
                slope = (ty - y) / (tx - x)
            if (sign, slope) not in slope_dict:
                slope_dict[(sign, slope)] = list()
            slope_dict[(sign, slope)].append((tx, ty))

    slope_dict_new = {key: sorted(slope_dict[key],
                                  key=lambda tup: pow(tup[0] - x, 2) + pow(tup[1] - y, 2), reverse=True)
                      for key in slope_dict}
    del slope_dict
    final_list = list()
    remain = True
    while remain:
        remain = False
        k = sorted(slope_dict_new.items())
        for key, value in k:
            if not value:  # already empty
                continue
            final_list.append(value.pop())
            if value:  # any non empty, not done yet
                remain = True

    print('Done')
    return final_list


if __name__ == '__main__':
    main()
