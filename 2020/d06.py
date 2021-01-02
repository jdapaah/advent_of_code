data = open('Input/d6.txt').read().split('\n\n')
count = sum(len(set(i)-{'\n'}) for i in data)
print(count)

count = 0
for i in data:
    s = set(i.split()[0])
    for j in i.split():
        s &= set(j)
    count += len(s)
print(count)
