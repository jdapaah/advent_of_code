with open('Input/d3.txt') as file:
	program = file.readline()

x1, y1 = 0, 0
x2, y2 = 0, 0
grid = {(x1, y1): 0}
for i in list(range(len(program)))[::2]:
	x1, y1 = {'^':(x1, y1+1), 'v':(x1, y1-1), '<':(x1-1, y1), '>':(x1+1, y1)}[program[i]]
        x2, y2 = {'^':(x2, y2+1), 'v':(x2, y2-1), '<':(x2-1, y2), '>':(x2+1, y2)}[program[i+1]]
	grid[(x1, y1)] = 0
	grid[(x2, y2)] = 0
print len(grid)
