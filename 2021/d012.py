data = [int(i) for i in open("Input/d1.txt").read().strip().split()]
nl = [data[i - 2] + data[i - 1] + data[i] for i in range(2, len(data))]
count = 0
for i in range(1, len(nl)):
    if nl[i - 1] < nl[i]:
        count += 1
print(count)
