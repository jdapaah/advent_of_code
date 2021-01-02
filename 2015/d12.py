with open('Input/d1.txt') as file:
	program = file.readline()

count = 0
for i, c in enumerate(program):
	count+= 2 * (c =='(') - 1
	if count == -1:
		print i+1
		exit()
