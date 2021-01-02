from re import finditer

data = open('Input/d20.txt').read().strip().split('\n\n')


def versions(tile):
    t1, r1, b1, l1 = tile[:10], tile[9::10], tile[-10:], tile[::10]
    t2, r2, b2, l2 = t1[::-1], r1[::-1], b1[::-1], l1[::-1]
    cc0 = t1, r1, b1, l1
    cc1 = r1, b2, l1, t2
    cc2 = b2, l2, t2, r2
    cc3 = l2, t1, r2, b1

    fl0 = t2, l1, b2, r1
    fl1 = l1, b1, r1, t1
    fl2 = b1, r2, t1, l2
    fl3 = r2, t2, l2, b2
    return cc0 + cc1 + cc2 + cc3 + fl0 + fl1 + fl2 + fl3


tiles = {}
poss = {}
one = ''
for tile in data:
    one, two = tile.split(':')
    one = int(one.split()[1])
    two = two.replace('\n', '')
    poss[one] = versions(two)
    tiles[one] = two

miny, minx = 0, 0
grid = {(0, 0): (one, 0)}
queue = [(0, 0)]
while queue:
    x, y = queue.pop()
    tile, inv = grid[x, y]
    border = poss[tile][4 * inv: 4 * (inv + 1)]
    for e, (i, j) in enumerate([(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]):
        if (i, j) in grid:
            continue
        shared_edge = border[e]
        found = False
        for t in poss:
            if shared_edge in poss[t] and t != tile:
                modind = (e + 2) % 4
                for ori in range(8):
                    if poss[t][modind + 4 * ori] == shared_edge:
                        grid[i, j] = (t, ori)
                        queue.append((i, j))
                        minx = min(minx, i)
                        miny = min(miny, j)
                        found = True
                        break
                if found:
                    break
grid = {(x - minx, y - miny): v for (x, y), v in grid.items()}
print(grid[0, 0][0] * grid[0, 11][0] * grid[11, 0][0] * grid[11, 11][0])


def all_rotations(sea):
    thing = [sea]
    tile = sea
    for inv in range(7):
        newtile = ''
        if inv == 3:
            tile = sea
            for i in range(96):
                newtile += tile[i*96:(i+1)*96][::-1]
        else:
            for i in reversed(range(96)):
                newtile += tile[i::96]
        tile = newtile
        thing.append(tile)
    return thing


def true_tile(i, j, tls):
    tile, inv = grid[i, j]
    tile = tls[tile]
    if inv > 3:
        newtile = ''
        for i in range(8):
            newtile += tile[i*8:(i+1)*8:][::-1]
        inv -= 4
        tile = newtile
    for _ in range(inv):
        newtile = ''
        for i in reversed(range(8)):
            newtile += tile[i::8]
        tile = newtile
    return tile


def merge():
    new_tiles = {}
    for tile in tiles:
        s = ''
        for j in range(100):
            i = j // 10
            j = j % 10
            if min(i, j) != 0 and max(i, j) != 9:
                s += tiles[tile][i * 10 + j]
        new_tiles[tile] = s
    sea = []
    for _ in range(96):
        sea.append([])
    for j in range(12):
        for i in range(12):
            string = true_tile(i, j, new_tiles)
            for y in range(8):
                sea[j*8 + y] += string[y*8:(y+1)*8]
    final_sea = ''
    while sea:
        final_sea = ''.join(sea.pop()) + final_sea
    return final_sea


pattern1 = '                  # '.replace(' ', '.')
pattern2 = '#    ##    ##    ###'.replace(' ', '.')
pattern3 = ' #  #  #  #  #  #   '.replace(' ', '.')
for version in all_rotations(merge()):
    count = 0
    pattern = '(?=(' + pattern1 + 76*'.' + pattern2 + 76*'.' + pattern3 + '))'
    for match in finditer(pattern, version):
        if match.start() % 96 < 76:
            count += 1
    if count:
        print(version.count('#') - count * 15)
