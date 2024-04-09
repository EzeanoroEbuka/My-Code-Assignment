count = 1
RANGE = 100
EVENLY = 2
 
while count < RANGE:
	count = count + 1
	if count % EVENLY == 0:
		print(count, end = " ")