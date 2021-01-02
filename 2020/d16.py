data = open('Input/d16.txt').read().strip().split('\n\n')
ruless = data[0].split('\n')
rules = []
for r in ruless:
    r1, r2 = r.split()[-3::2]
    ran1 = range(int(r1[:r1.index('-')]),
                 int(r1[r1.index('-') + 1:]) + 1)
    ran2 = range(int(r2[:r2.index('-')]),
                 int(r2[r2.index('-') + 1:]) + 1)
    rules.append((ran1, ran2))
mine = [int(i) for i in data[1].split('\n')[1].split(',')]
nearby = [[int(j) for j in i.split(',')] for i in data[2].split('\n')[1:]]

count = 0
for ticket in nearby[:]:
    for val in ticket:
        goodval = False
        for ran1, ran2 in rules:
            if val in ran1 or val in ran2:
                goodval = True
                break # unecessary
        if not goodval:
            count+=val
            nearby.remove(ticket) #pt 2
            break  # break unecessary, there is only one bad val per ticket
print(count)

poss = {i:list(range(len(rules))) for i in range(len(rules))} # index of ticket: possible indices of rules
field = []
for i in range(len(rules)): # field = transpose(nearby)
    field.append([])
for ticket in nearby:
    for ind, val in enumerate(ticket):
        field[ind].append(val)
for i, vals in enumerate(field):
    for j, (ran1, ran2) in enumerate(rules):
        for val in vals:
            if val not in ran1 and val not in ran2:
                poss[i].remove(j)
                break
orderedkeys = sorted(poss, key=lambda l: len(poss[l])) # sorted by increasing number of rule options
k = 1
while orderedkeys:
    tind = orderedkeys[0]
    rule = poss[tind][0]
    for j in orderedkeys:
        poss[j].remove(rule)
    if rule < 6:
        k*=mine[tind]
    poss.pop(tind)
    orderedkeys.pop(0)
print(k)
