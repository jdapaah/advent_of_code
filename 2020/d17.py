grid = [[[int(el == '#') for el in row] for row in
         open('Input/d17.txt').read().strip().split()]]

def valid3(g, i, j, k):
    return min(i, j, k) >= 0 and \
           i < len(g) and \
           j < len(g[0]) and \
           k < len(g[0][0])

def neighbors3(g, r, c, d, exists):
    return (exists and -g[r][c][d]) + \
           sum(sum(sum(valid3(g, i, j, k) and g[i][j][k]
                       for k in range(d-1, d+2))
                   for j in range(c - 1, c + 2))
               for i in range(r - 1, r + 2))

def evolve3(g):
    ngrid = []
    for i in range(len(g)+2):
        ngrid.append([])
        for j in range(len(g[0])+2):
            ngrid[i].append([])
            for k in range(len(g[0][0])+2):
                exists = valid3(g, i-1, j-1, k-1)  # checks if existing value
                count = neighbors3(g, i-1, j-1, k-1, exists)
                if count == 3 or exists and grid[i-1][j-1][k-1] and count == 2:
                    ngrid[i][j].append(1)
                else:
                    ngrid[i][j].append(0)
    return ngrid
for _ in range(6):
    grid = evolve3(grid)
print(sum(sum(sum(col) for col in row) for row in grid))

"""Make it a tesseract"""
grid = [[[[int(el == '#') for el in row] for row in
         open('Input/d17.txt').read().strip().split()]]]

def valid4(g, i, j, k, l):
    return i in range(len(g)) and \
           j in range(len(g[0])) and \
           k in range(len(g[0][0])) and \
           l in range(len(g[0][0][0]))

def neighbors4(g, r, c, d, m, exists):
    if exists:
        t = -g[r][c][d][m]
    else:
        t = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            for k in range(d-1, d+2):
                for l in range(m-1, m+2):
                    if valid4(g, i, j, k, l):
                        t += g[i][j][k][l]
    return t

def evolve4(g):
    ngrid = []
    for i in range(len(g)+2):
        ngrid.append([])
        for j in range(len(g[0])+2):
            ngrid[i].append([])
            for k in range(len(g[0][0])+2):
                ngrid[i][j].append([])
                for l in range(len(g[0][0][0])+2):
                    exists = valid4(g, i-1, j-1, k-1, l-1)
                    count = neighbors4(g, i-1, j-1, k-1, l-1, exists)
                    if count == 3 or exists and g[i-1][j-1][k-1][l-1] and count == 2:
                        ngrid[i][j][k].append(1)
                    else:
                        ngrid[i][j][k].append(0)
    return ngrid
for _ in range(6):
    grid = evolve4(grid)
print(sum(sum(sum(sum(depth) for depth in col) for col in row) for row in grid))