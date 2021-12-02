data = [int(i) for i in open("Input/d1.txt").read().strip().split()]
count = 0
for i in range(1, len(data)):
    if data[i - 1] < data[i]:
        count += 1
print(count)