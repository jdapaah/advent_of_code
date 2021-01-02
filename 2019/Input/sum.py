with open('d13.txt') as file:
	a = sum([int(k) for k in file.read().split(',')])
print(a)
