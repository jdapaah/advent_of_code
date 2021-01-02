def loop(d):
    acc = 0
    pointer = 0
    called = set()
    while pointer < len(d):
        a = d[pointer].split()
        ins = a[0]
        if pointer in called:
            return True, acc
        called.add(pointer)
        if ins == 'acc':
            acc += int(a[1])
            pointer += 1
        elif ins == 'jmp':
            pointer += int(a[1])
        elif ins == 'nop':
            pointer += 1
    return False, acc

data = open('Input/d8.txt').read().strip().split('\n')
print(loop(data)[1])

for i in range(len(data)):
    command = data[i].split()
    if command[0] == 'nop':
        data[i] = 'jmp ' + command[1]
        val = loop(data)
        if not val[0]:
            print(val[1])
        data[i] = 'nop ' + command[1]
    elif command[0] == 'jmp':
        data[i] = 'nop ' + command[1]
        val = loop(data)
        if not val[0]:
            print(val[1])
        data[i] = 'jmp ' + command[1]
