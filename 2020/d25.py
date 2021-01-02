data = open('Input/d25.txt').read().strip().split('\n')
cardpk = int(data[0])
doorpk = int(data[1])
d = key = 1
while d != doorpk:
    d = (d * 7) % 20201227
    key = (key * cardpk) % 20201227
print(key)
