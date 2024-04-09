MULTIPLE = 10
total = 0
count = 1
while count < 20000:
	count = count + 1
	if(count % MULTIPLE == 0):
		total += count
print(total)