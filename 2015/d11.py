with open('Input/d1.txt') as file:
	program = file.readline()
print(program.count('(')-program.count(')'))
