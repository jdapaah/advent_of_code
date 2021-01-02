a = 0
with open('Input/d1.txt') as file:
    for line in file:
        b = int(line)
        while b:
            b = max(0, b // 3 - 2)
            a += b
print(a)
