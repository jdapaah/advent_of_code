from re import fullmatch, search
rs, data = open('Input/d19.txt').read().strip().split('\n\n')
# rs, data = open('test.txt').read().strip().split('\n\n')

rules = {}
for r in rs.split('\n'):
    rind, rule = r.split(': ')
    rules[rind] = rule.split()

def build1(rules, i):
    string = ""
    add = False
    for rule in rules[i]:
        if str.isdigit(rule):
            string += '(' + build1(rules, rule) + ')'
        elif rule == '|':
            string = '(' + string + ')|('
            add = True
        elif rule[0] == '"':
            return rule[1]
    if add:
        string +=')'
    return string

pattern = build1(rules, '0')
print(sum(fullmatch(pattern, string)!=None for string in data.split()))
# 42 42 31
rules['8']  += '| 42 8'.split()
rules['11'] += '| 42 11 31'.split()
# should be 42 * (x + y) + 31 * y

p31 = build1(rules, '31')
p42 = build1(rules, '42')
len42 = len(search(p31, data).group(0))  # 8
len31 = len(search(p42, data).group(0))  # 8

count = 0
for string in data.split():
    y = 0
    while fullmatch(p31, string[-8:]) != None:
        string = string[:-8]
        y+=1
    if y==0: # did not match 11 pt 2
        continue
    while fullmatch(p42, string[-8:]) != None:
        string = string[:-8]
        y-=1
    if not string and y<0 : # string has been vacated, and 8 is counted
        count+=1
print(count)



