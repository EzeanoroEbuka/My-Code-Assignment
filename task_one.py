passed = 0
failed = 0
result = 0
count = 0
while result != 2 and result != 1:
	result = int(input("Enter result ,press 1 or 2 to stop \n"))
	if result >= 45:
		passed = passed + 1
		 
	elif result > 2:
		failed = failed + 1

print("Passed",passed)
print("Failed",failed)

if passed > 8:
	print('Bonus to Instructor')

