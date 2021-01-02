data = open('Input/d21.txt').read().strip().split('\n')
ings = []
possible_foods = {}

for line in data:
    ingl, allist = line.split(' (contains ')
    ingl  = ingl.split()
    allist = allist[:-1].split(', ')
    ings += ingl

    for alle in allist:
        if alle not in possible_foods:
            possible_foods[alle]  = set(ingl)
        else:
            possible_foods[alle] &= set(ingl)

fwa = set()  # foods with allergens
for foodset in possible_foods.values():
    fwa |= foodset
print(sum(ing not in fwa for ing in ings))

fta = {}  # food : allegen dictionary
while len(fta) != len(possible_foods):
    for alle, fset in possible_foods.items():
        if len(fset) == 1:
            food = fset.pop()
            fta[food] = alle
            for alle in possible_foods:
                possible_foods[alle].discard(food)

fta = sorted(fta.keys(), key=lambda k: fta[k])
for i in range(len(fta)-1):
    print(fta[i], end=',')
print(fta[-1])