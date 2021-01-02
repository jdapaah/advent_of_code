grid = open('Input/d3.txt').read().strip().split()

i, j = 0, 0
count = 0
while i < len(grid):
    if grid[i][j % len(grid[0])] == "#":
        count += 1
    i += 1
    j += 3
print(count)

product = 1
for a, b in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    i, j = 0, 0
    count = 0
    while i < len(grid):
        if grid[i][j % len(grid[0])] == "#":
            count += 1
        i += b
        j += a
    product *= count

print(product)
