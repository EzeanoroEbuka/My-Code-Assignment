digits = int(input("Enter Digit \n"))

count = 1
for number in range(5):
	converter = (100000 / (count * 10))
	digit = digits // converter
	digits = digits % converter
	count *= 10
	print(f"{digit:.0f}  ",end = " ")