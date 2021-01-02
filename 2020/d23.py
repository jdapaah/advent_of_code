from time import perf_counter
inp = '562893147'
data = {int(inp[i - 1]): int(inp[i]) for i in range(9)}
curr = int(inp[0])


def move(curr):
    moved = {}
    a, b = data[curr], 0
    ms = a  # first element in moved
    for i in range(3):
        b = data.pop(a)
        moved[a] = b
        a = b
    data[curr] = b
    dest = curr-1
    if 1 in moved:
        if 2 in moved:
            if 3 in moved:
                mincup = 4
            else:
                mincup = 3
        else:
            mincup = 2
    else:
        mincup = 1

    # mincup = min(data)
    while dest not in data:
        dest -= 1
        if dest < mincup:
            mil = pow(10, 6)
            # dest = max(data)
            if mil in moved:
                if mil-1 in moved:
                    if mil-2 in moved:
                        dest = mil-3
                    else:
                        dest = mil-2
                else:
                    dest = mil-1
            else:
                dest = mil
    b = data[dest]
    data[dest] = ms
    for i in range(2):
        data[ms] = moved[ms]
        ms = data[ms]
    data[ms] = b
    curr = data[curr]
    return curr


for _ in range(100):
    curr = move(curr)
k = 1
for i in range(8):
    print(data[k], end='\n'*(i//7))
    k = data[k]

data = {int(inp[i - 1]): int(inp[i]) for i in range(9)}
curr = int(inp[0])

for i in range(10, pow(10, 6)):
    data[i] = i+1
data[int(inp[-1])] = 10
data[pow(10, 6)] = curr
start = perf_counter()
for i in range(pow(10, 7)):
    curr = move(curr)
print(data[1] * data[data[1]])

