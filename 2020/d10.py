data = sorted([int(i) for i in open('Input/d10.txt').read().strip().split('\n')])

count1 = (data[0] == 1)
count3 = (data[0] == 3) + 1
for i in range(len(data)-1):
    count1 += (data[i+1]-data[i] == 1)
    count3 += (data[i+1]-data[i] == 3)
print(count3 * count1)

ways = {0:1}
for i in data:
    ways[i] = ways.get(i-3, 0) + ways.get(i-2, 0) + ways.get(i-1, 0)
print(ways[data[-1]])
