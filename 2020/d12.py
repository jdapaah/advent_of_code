data = open('Input/d12.txt').read().strip().split('\n')
i, j = 0, 0
dir = 0 # E, S 3
for ins in data:
    d = ins[0]
    val = int(ins[1:])
    if d =='N':
        j +=val
    elif d=='S':
        j -=val
    elif d=='E':
        i +=val
    elif d=='W':
        i -=val
    elif d=='R':
        dir =(dir-val/90)%4
    elif d=='L':
        dir =(dir+val/90)%4
    elif d=='F':
        if dir == 1:
            j += val
        elif dir == 3:
            j -= val
        elif dir == 0:
            i += val
        elif dir == 2:
            i -= val
print(abs(i) + abs(j))

i, j = 0, 0
wi, wj = 10, 1
for ins in data:
    d = ins[0]
    val = int(ins[1:])
    di = wi - i
    dj = wj - j
    if d =='N':
        wj +=val
    elif d=='S':
        wj -=val
    elif d=='E':
        wi +=val
    elif d=='W':
        wi -=val
    elif ins in ['R90', 'L270']:
        wi = i + dj
        wj = j - di
    elif val==180:
        wi = i - di
        wj = j - dj
    elif ins in ['L90', 'R270']:
        wi = i - dj
        wj = j + di
    elif d == 'F':
        i += di * val
        j += dj * val
        wi += di * val
        wj += dj * val
print(abs(i) + abs(j))





