count = 0
with open('Input/d2.txt') as file:
	for line in file:
		p = [int(num) for num in line.strip().split('x')]
		a  = [p[0]*p[1], p[1]*p[2], p[0]*p[2]]
		count += 2*sum(a) + min(a) 
print count

