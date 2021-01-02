data = [0,5,4,1,10,14,7]
for k in 2020, 30000000:
    d = {}
    for i in range(len(data) - 1):
        d[data[i]] = i
    last = data[-1]
    for i in range(len(d.keys()), k):
        if i == k-1:
            print(last)
        if last in d:
            age = i-d[last]
        else:
            age = 0
        d[last] = i
        last = age
