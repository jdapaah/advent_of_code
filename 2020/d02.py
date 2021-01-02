data = [i.split() for i in open("Input/d2.txt").read().strip().split('\n')]

count = 0
for i in data:
    lim = i[0].split('-')
    count += int(lim[0]) <= i[2].count(i[1][0]) <= int(lim[1])
print(count)

count = 0
for i in data:
    lim = i[0].split('-')
    count += (i[2][int(lim[0]) - 1] == i[1][0]) ^ (i[2][int(lim[1]) - 1] == i[1][0])
print(count)
