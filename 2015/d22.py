count = 0
with open('Input/d2.txt') as file:
	for line in file:
		p = [int(num) for num in line.strip().split('x')]
		a = min(p)
		p.remove(a)
		b = min(p)
		p.remove(b)
		count += 2*(a+b) + a*b*p.pop()
print count
