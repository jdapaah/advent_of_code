def main():
    best = (-1, (0, 0))
    count = 0
    with open('Input/test.txt') as file:
        field = [line.strip() for line in file]
    for i, row in enumerate(field):  # dist from top
        for j, el in enumerate(row):  # dist from left
            if el == '#':
                count += 1
                best = max(best, visible(field, i, j))

    print('Number of total asteroids', count)
    print('Best line of sight is found at %s; we can see %d asteroids' % (best[1], best[0]))


def visible(field, i, j):  # edit to get the closest asteroid first
    # get the distance if the slope is found again, update if closer
        # small sort by distance?
    # sort by slope to get them in order
    slope_field = set()
    count = 0
    for tempi, row in enumerate(field):
        for tempj, el in enumerate(row):
            if tempi == i or tempj == j or el == '.':
                continue
            sign = (tempi - i) / abs(tempi - i)
            s = (tempj - j) / (tempi - i), sign
            if s not in slope_field:
                count += 1
                slope_field.add(s)

    for tempi in range(i - 1, -1, -1):
        if field[tempi][j] == '#':
            count += 1
            break
    for tempi in range(i + 1, len(field)):
        if field[tempi][j] == '#':
            count += 1
            break
    for tempj in range(j - 1, -1, -1):
        if field[i][tempj] == '#':
            count += 1
            break
    for tempj in range(j + 1, len(field[0])):
        if field[i][tempj] == '#':
            count += 1
            break

    return count, (i, j)


if __name__ == '__main__':
    main()
