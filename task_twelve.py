user_input = int(input("Enter five number: "))

original_number = user_input
reverse_number = 0
SEPERATORS = 10
for number in range(5):
	sample = user_input % SEPERATORS
	reverse_number = (reverse_number * SEPERATORS) + sample
	user_input = (user_input // SEPERATORS)

if reverse_number == original_number:
	print("A Palindrome")

else:
	print("Not A Palindrome")