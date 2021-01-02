data = open('Input/d24.txt').read().strip().split('\n')
tiles = {}
for line in data:
    i = 0
    x, y = 0, 0
    while i < len(line):
        if line[i] == 'e':
            x+=1
        elif line[i] == 'w':
            x-=1
        elif line[i] in 'ns':
            y+=1
            if line[i] == 's':
                y-=2
            i+=1
            if line[i] == 'e':
                x+=.5
            elif line[i] == 'w':
                x-=.5
        i+=1
    if (x, y) in tiles:
        tiles[x, y] = not tiles[x, y]
    else:
        tiles[x, y] = True
print(sum(i for i in tiles.values()))


def state(t, tx, ty):
    count = 0
    for x, y in [(tx + 1, ty), (tx + .5, ty - 1), (tx + .5, ty + 1),
                 (tx - 1, ty), (tx - .5, ty - 1), (tx - .5, ty + 1)]:
        count += t.get((x, y), 0)
    if (count == 0 or count > 2) and t.get((tx, ty), False):
        return False
    if count == 2 and t.get((tx, ty), False) == False:
        return True
    return -1


for i in range(100):
    new_tiles = {}
    for sx, sy in tiles:
        around = [(sx + 1, sy), (sx + .5, sy - 1), (sx + .5, sy + 1), (sx, sy),
                  (sx - 1, sy), (sx - .5, sy - 1), (sx - .5, sy + 1)]
        for tile in around:
            if tile in new_tiles:
                continue
            ns = state(tiles, tile[0], tile[1])
            if ns != -1:
                new_tiles[tile] = ns
        if (sx, sy) not in new_tiles:
            new_tiles[sx, sy] = tiles[sx, sy]

    tiles = new_tiles
print(sum(i for i in tiles.values()))



