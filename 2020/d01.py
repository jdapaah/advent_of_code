data = [int(i) for i in open("Input/d1.txt").read().strip().split()]

for i in data:
    if 2020 - i in data:
        print(i * (2020-i))
        break
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if 2020 - data[i] - data[j] in data:
            print(data[i] * data[j] * (2020 - data[i] - data[j]))
            exit()
