count = 0
with open('Input/d5.txt') as file:
	for l in file:
		if l.count('xy') + l.count('ab') + l.count('cd')+l.count('pq'):
			continue
		if l.count('a')+l.count('e')+l.count('i')+l.count('o')+l.count('u')<3:
			continue
		
			
		
