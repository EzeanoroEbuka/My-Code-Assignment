count = 1
MULTIPLE = 3
RANGE = (MULTIPLE * 15) 
REMAINDER = 0
total = 0
while count < RANGE:
	count = count + 1
	if count % MULTIPLE == REMAINDER:
		total = count
		print(total)

