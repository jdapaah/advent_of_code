x, y, a = 0, 0, 0
for i in open("Input/d2.txt").readlines():
    d, j = i.split()
    j = int(j)
    if d == 'forward':
        x += j
        y += a * j
    elif d == 'up':
        a -= j
    else:
        a += j

print(x * y)
