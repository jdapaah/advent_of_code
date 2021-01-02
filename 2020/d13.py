from math import inf
data = open('Input/d13.txt').read().strip().split('\n')
stop = int(data[0])
buses = data[1].split(',')
cval = inf
diff = 0
fid = -1
for i in buses:
    if i=='x':
        continue
    val = int(i) - stop%int(i)
    if val < cval:
        cval = val
        diff = val
        fid = int(i)

print(diff * fid)

N = 1
x = 0
numbers = [int(i) for i in buses if str.isdigit(i)]
for i in numbers:
    N*=i
for a in range(len(buses)):
    if buses[a] =='x':
        continue
    n = int(buses[a])
    y = N//n
    z = pow(y, -1, n)
    x += y * z * (n-a)
print(x%N)
