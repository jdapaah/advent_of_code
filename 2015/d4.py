from hashlib import md5
i = 0
while md5("bgvyzdsv"+str(i)).hexdigest()[:6] != '0'*6:
	i+=1
print i 
