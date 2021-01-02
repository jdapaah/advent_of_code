data = open('Input/d7.txt').read().strip().split('\n')

count = 0
d = {}
for line in data:
    a = line.split('s contain ')
    d[a[0]] = []
    for i in a[1].split(', '):
        d[a[0]].append(i.rstrip("s."))

for bag, smaller_bags in d.items():
    queue = smaller_bags[:]
    while queue:
        og = queue.pop()
        new_bag = og[og.index(' ')+1:]
        if og == 'no other bag':
            continue
        elif new_bag == 'shiny gold bag':
            count += 1
            break
        else:
            queue += d[new_bag]
print(count)

count = 0
queue = d['shiny gold bag']
while queue:
    og = queue.pop()
    if og == 'no other bag':
        continue
    ind = og.index(' ')+1
    for i in range(int(og[:ind])):
        count += 1
        queue += d[og[ind:]]
print(count)
