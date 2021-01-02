def main():
	with open('Input/d16.txt') as file:
		program = file.readline().strip()
	print(''.join(program[:8]))
	for i in range(100):
		program = process(program, len(program))
	print(''.join(program[:8]))


def process(program, k):
	new_pro = []
	for i in range(k):
		val = 0
		ind = 1
		pattern = create(i)
		for num2 in program:
			val += int(num2) * pattern[ind % (4*(i+1))]
			ind += 1
		new_pro.append(str(abs(val) % 10))
	return new_pro


def create(i):
	return [0] * (i + 1) + [1] * (i + 1) + [0] * (i + 1) + [-1] * (i + 1)


if __name__ == '__main__':
	main()
