data = open('Input/d18.txt').read().strip().split('\n')

def match(s, i):
    left = 1
    i+=1
    while left:
        if s[i] == '(':
            left+=1
        elif s[i] == ')':
            left-=1
        i+=1
    return i-1

def evaluate1(string):
    i = 0
    while i < len(string):  # evaluate parantheticals
        if string[i] == '(':
            ind = match(string, i)
            string = string[:i] + str(evaluate1(string[i+1: ind])) + string[ind + 1:]
        i += 1

    string = string.split()
    while len(string)>1:  # single value
        string = [str(eval(''.join(string[:3])))] + string[3:]  # evaluate first 3 characters
    return int(string[0])

def evaluate2(string):  # split by mults when left == 0
    i = 0
    while i < len(string):  # evaluate parantheticals
        if string[i] == '(':
            ind = match(string, i)
            string = string[:i] + str(evaluate2(string[i+1: ind])) + string[ind+1:]
        i+=1

    k = 1
    for ex in string.split('*'):  # split into multiplicative pieces
        k *= eval(ex) # should all be sum expressions
    return k

print(sum(evaluate1(ex) for ex in data))
print(sum(evaluate2(ex) for ex in data))
