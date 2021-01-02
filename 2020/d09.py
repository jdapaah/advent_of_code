from time import perf_counter
start = perf_counter()
data = [int(i) for i in open('Input/d9.txt').read().strip().split('\n')]

target = 0
for i in range(25, len(data)):
    preamble = data[i-25:i]
    b = False
    for j in preamble:
        if data[i]-j in preamble:
            b = True
            break
    if not b:
        target = data[i]
        print(target)
        break

for j in range(i):
    s = 0
    k = j
    while s<target:
        s+=data[k]
        k+=1;
    if s==target:
        print(max(data[j:k]) + min(data[j:k]))
        exit()


