print("Enter two Integer,and I will tell you",'the relationships they satisfy.')

number1 = int(input("Enter first Integer \n"))

number2 = int(input(" Enter second Integer \n"))

print()
if number1 == number2:
	print(number1, 'is equal to', number2)
else:
	print(number1, 'is not equal to', number2)

if number1 < number2:
	print(number1, 'is less than', number2)	
else:
	print(number1, 'is greater than', number2)

if number1 <= number2:
	print(number1, 'is less than or equal to', number2)	
else:
	print(number1, 'is greater than or equal to', number2)