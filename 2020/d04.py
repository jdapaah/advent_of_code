data = open('Input/d4.txt').read().split('\n\n')

print(sum({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <=
             {j.strip()[:3] for j in i.split()} for i in data))

count = 0
for i in data:
    l = set()
    works = True
    for j in i.split():
        k = j.strip()[:3]
        v = j.strip()[4:]
        l.add(k)

        if k == 'byr':
            if not (1920 <= int(v) <= 2002):
                works = False

        elif k == 'iyr':
            if not (2010 <= int(v) <= 2020):
                works = False

        elif k == 'eyr':
            if not (2020 <= int(v) <= 2030):
                works = False

        elif k == 'hgt':
            if v[-2:] == 'in':
                if not (59 <= int(v[:-2]) <= 76):
                    works = False
            elif v[-2:] == 'cm':
                if not (150 <= int(v[:-2]) <= 193):
                    works = False
            else:
                works = False

        elif k == 'hcl':
            if not (v[0] == '#' and len(v) == 7 and set(v[1:]) < set("abcdef1234567890")):
                works = False

        elif k == 'pid':
            if not (len(v) == 9 and v.isdigit()):
                works = False

        elif k == 'ecl':
            if v not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                works = False

    count += works and {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= l
print(count)
