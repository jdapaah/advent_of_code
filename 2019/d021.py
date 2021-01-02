program = []
with open('Input/d2.txt') as file:
	program = file.readline().split(',')

for ind, num in enumerate(program):
	program[ind] = int(num)


in_pointer = 0
opcode = program[in_pointer]
while opcode != 99:
	
	addr1 = program[in_pointer + 1]
	addr2 = program[in_pointer + 2]
	addr3 = program[in_pointer + 3]
	
	num1 = program[addr1]
	num2 = program[addr2]

	if opcode == 1:
		program[addr3] = num1 + num2
	elif opcode == 2:
		program[addr3] = num1 * num2
	else:
		print('Something is wrong, bad opcode')
		exit(2)

	in_pointer += 4
	opcode = program[in_pointer]

print(program[0])
