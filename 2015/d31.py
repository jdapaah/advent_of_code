with open('Input/d3.txt') as file:
	program = file.readline()

x, y = 0, 0
grid = {(x, y): 0}
for c in program:
	x, y = {'^':(x, y+1), 'v':(x, y-1), '<':(x-1, y), '>':(x+1, y)}[c]
	grid[(x, y)] = 0
print len(grid)
