from copy import deepcopy as copy

data0 = open('Input/d11.txt').read().strip().split()
for ind, string in enumerate(data0):
    data0[ind] = list(string)


def count1(i, j, d):
    c = 0
    if i + 1 < len(d) and j > 0 and d[i + 1][j - 1] == '#':
        c += 1
    if i + 1 < len(d) and d[i + 1][j] == '#':
        c += 1
    if i + 1 < len(d) and j + 1 < len(d[0]) and d[i + 1][j + 1] == '#':
        c += 1
    if j > 0 and d[i][j - 1] == '#':
        c += 1
    if j + 1 < len(d[0]) and d[i][j + 1] == '#':
        c += 1
    if i > 0 and j > 0 and d[i - 1][j - 1] == '#':
        c += 1
    if i > 0 and d[i - 1][j] == '#':
        c += 1
    if i > 0 and j + 1 < len(d[0]) and d[i - 1][j + 1] == '#':
        c += 1
    return c


def count2(i, j, d):
    c = 0
    i0, j0 = i + 1, j - 1
    while i0 < len(d) and j0 >= 0 and d[i0][j0] == '.':
        i0 += 1
        j0 -= 1
    if i0 < len(d) and j0 >= 0 and d[i0][j0] == '#':
        c += 1
    i0 = i + 1
    while i0 < len(d) and d[i0][j] == '.':
        i0 += 1
    if i0 < len(d) and d[i0][j] == '#':
        c += 1
    i0, j0 = i + 1, j + 1
    while i0 < len(d) and j0 < len(d[0]) and d[i0][j0] == '.':
        i0 += 1
        j0 += 1
    if i0 < len(d) and j0 < len(d[0]) and d[i0][j0] == '#':
        c += 1
    j0 = j - 1
    while j0 >= 0 and d[i][j0] == '.':
        j0 -= 1
    if j0 >= 0 and d[i][j0] == '#':
        c += 1
    j0 = j + 1
    while j0 < len(d[0]) and d[i][j0] == '.':
        j0 += 1
    if j0 < len(d[0]) and d[i][j0] == '#':
        c += 1
    i0, j0 = i - 1, j - 1
    while i0 >= 0 and j0 >= 0 and d[i0][j0] == '.':
        i0 -= 1
        j0 -= 1
    if i0 >= 0 and j0 >= 0 and d[i0][j0] == '#':
        c += 1
    i0 = i - 1
    while i0 >= 0 and d[i0][j] == '.':
        i0 -= 1
    if i0 >= 0 and d[i0][j] == '#':
        c += 1
    i0, j0 = i - 1, j + 1
    while i0 >= 0 and j0 < len(d[0]) and d[i0][j0] == '.':
        i0 -= 1
        j0 += 1
    if i0 >= 0 and j0 < len(d[0]) and d[i0][j0] == '#':
        c += 1
    return c


new_data = copy(data0)
data = copy(data0)
change = True
while change:
    change = False
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'L' and count1(i, j, data) == 0:
                new_data[i][j] = '#'
                change = True
            elif data[i][j] == '#' and count1(i, j, data) >= 4:
                new_data[i][j] = 'L'
                change = True
    data = copy(new_data)
print(sum(i.count('#') for i in data))

new_data = copy(data0)
data = copy(data0)
change = True
while change:
    change = False
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'L' and count2(i, j, data) == 0:
                new_data[i][j] = '#'
                change = True
            elif data[i][j] == '#' and count2(i, j, data) >= 5:
                new_data[i][j] = 'L'
                change = True
    data = copy(new_data)
print(sum(i.count('#') for i in data))
