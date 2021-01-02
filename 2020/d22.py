from copy import deepcopy
data = open('Input/d22.txt').read().strip().split('\n\n')
# data = open('test.txt').read().strip().split('\n\n')
p1 = [int(i) for i in data[0].split()[2:]]
p2 = [int(i) for i in data[1].split()[2:]]

def combat(one, two):
    while one and two:
        a = one.pop(0)
        b = two.pop(0)
        if a>b:
            one.append(a)
            one.append(b)
        else:
            two.append(b)
            two.append(a)
    k = 0
    if one:
        for i in range(len(one)):
            k += one[i] * (len(one)-i)
    else:
        for i in range(len(two)):
            k += two[i] * (len(two)-i)
    return k, one!=[]

def rcombat(one, two):
    game_states = set()
    while one and two:
        gs = tuple(one), tuple(two)
        if gs in game_states:
            return sum(one[i] * (len(one)-i) for i in range(len(one))), True
        game_states.add(gs)
        a = one.pop(0)
        b = two.pop(0)
        if a <= len(one) and b <= len(two):
            onewins = rcombat(deepcopy(one[:a]), deepcopy(two[:b]))[1]
            if onewins:
                one.append(a)
                one.append(b)
            else:
                two.append(b)
                two.append(a)
        else:
            if a > b:
                one.append(a)
                one.append(b)
            else:
                two.append(b)
                two.append(a)

    if one:
        return sum(one[i] * (len(one) - i) for i in range(len(one))), True
    else:
        return sum(two[i] * (len(two) - i) for i in range(len(two))), False


print(combat(p1[:], p2[:])[0])
print(rcombat(p1[:], p2[:])[0])









