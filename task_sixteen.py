first_largest_number = 0
second_largest_number = 0
list1 = []
for numbers in range(10):
	numbers = int(input("Enter number: "))
	list.append(numbers)
for number in numbers:
	if number > first_largest_number:
		first_largest_number = number

	if first_largest_number > number and number > second_largest_number:
		 second_largest_number = number
	
		
print(f"First Largest Number is: {first_largest_number}\nSecond largest Number is: {second_largest_number}")