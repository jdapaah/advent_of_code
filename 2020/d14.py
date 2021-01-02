data = open('Input/d14.txt').read().strip().split('\n')

memory = {}
for line in data:
    if line.startswith('mask'):
        mask = line[7:]
    else:
        a = line.split(' = ')
        address = a[0][4:-1]
        val = bin(int(a[1]))[2:]
        val = '0' * (36 - len(val)) + val
        if address not in memory:
            memory[address] = val
        new_string = ['0'] * 36
        for i in range(36):
            if mask[i] !='X':
                new_string[i] = mask[i]
            else:
                new_string[i] = val[i]
        memory[address] = ''.join(new_string)
print(sum(int(v, 2) for v in memory.values()))

def combo(add):
    l = [add]
    c = []
    while l:
        a = l.pop(0)
        if 'X' in a:
            a0 = a[:]
            a0[a0.index('X')] = '0'
            l.append(a0)
            a1 = a
            a1[a1.index('X')] = '1'
            l.append(a1)
        else:
            c.append(''.join(a))
    return c

memory = {}
for line in data:
    if line.startswith('mask'):
        mask = line[7:]
    else:
        a = line.split(' = ')
        address = a[0][4:-1]
        addbin = bin(int(address))[2:]
        addbin = '0' * (36-len(addbin)) + addbin
        val = bin(int(a[1]))[2:]
        val = '0' * (36-len(val)) + val
        new_string = list(addbin)
        for i in range(36):
            if mask[i] in ['1', 'X']:
                new_string[i] = mask[i]
        for j in combo(new_string):
            memory[j] = val
print(sum(int(v, 2) for v in memory.values()))




