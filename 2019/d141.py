from queue import SimpleQueue
# queue = SimpleQueue()
equations = dict()
bases = list()


def main():
	global equations, bases
	with open('Input/test.txt') as file:
		for line in file:
			sides = line.strip().split(' => ')
			prod = sides[1].split()
			reacs = [int(prod[0])]
			for c in sides[0].split(', '):
				r = c.split()
				r[0] = int(r[0])
				reacs.append(tuple(r))
				if r[0] == "ORE":  # prod is a base chemical
					bases.append(prod[1])
			equations[prod[1]] = reacs

	for k, v in equations.items():
		print(k, v)

	get_ore()


#
# 	for reactant in equations['FUEL'][1:]:
# 		go_to_root(reactant, 1)
# 	print(bases)
#
# 	final = 0
# 	for chem in bases:
# 		overestimate = 0
# 		while overestimate < bases[chem]:
# 			overestimate += equations[chem][0] * equations[chem][1][1]
# 		final += overestimate
# 	print(final)
#
#
# def go_to_root(ingred, k):
# 	name = ingred[0]
# 	if name in bases:
# 		bases[name] += k * ingred[1]
# 	else:
# 		for reactant in equations[name][1:]:
# 			go_to_root(reactant,  k * equations[name][0] * ingred[1])
def get_ore():
	available_ore = 0
	# queue.put('FUEL')
	queue = ['FUEL']
	while queue:
		# order = queue.get()
		order = queue.pop(0)
		for i in equations[order][1:]:
			for j in range(i[0]):
				# queue.put(i[1])
				queue.append(i[1])


if __name__ == '__main__':
	main()
