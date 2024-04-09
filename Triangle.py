num = int(input("Enter Input \n"))

row = 0
while(row <= num):
	row = row + 1
	column = 1
	while(column <= row):
		column = column + 1
		print("*",end = " ")
	print(" ")