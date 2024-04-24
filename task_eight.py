sum = 0
largest = 0
product = 1 
smallest = 0

for numbers in range(0,4,1):
	values = int(input("Enter Integers \n"))
	if values > largest:
		largest = values
	elif values < smallest:
		smallest = values
	elif largest > smallest:
		smallest = values
	if smallest == 0:
		smallest = values
	product *= values
	sum += values
average = sum / 4
	
print(f"The Sum is: {sum}\nThe Average is: {average}\nThe Product is: {product}\nThe largest number is: {largest}\nThe Smallest number is:{smallest}")