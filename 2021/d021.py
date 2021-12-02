x, y = 0, 0
for i in open("Input/d2.txt").readlines():
    d, j = i.split()
    j = int(j)
    if d == 'forward':
        x += j
    elif d == 'up':
        y -= j
    else:
        y+=j
print(x*y)
