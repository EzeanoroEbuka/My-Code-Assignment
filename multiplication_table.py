number = int(input("Enter Number"))
count = 0
total = 0
while count < 10:
	count = count + 1
	total = number * count
	print(str(number) + " " + "*"  +" " + str(count) +  "  " + "=" + "  " + str(total)) 