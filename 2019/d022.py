def main():
	program_A = []
	with open('Input/d2.txt') as file:
		program_A = file.readline().split(',')

	for ind, num in enumerate(program_A):
		program_A[ind] = int(num)

	for i in range(100):
		for j in range(100):
			if get_num(i, j, program_A[:]) == 19690720:
				print( i * 100 + j )
				exit(0)


def get_num(a, b, program):

	program[1] = a
	program[2] = b

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

	return program[0]


if __name__ == '__main__':
	main()