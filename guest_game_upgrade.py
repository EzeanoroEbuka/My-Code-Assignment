import  random
correct_number = random.randrange(1,10)

guest = int(input("Guest a number Between  \n"))

while(correct_number != guest):
		guest = int(input("Guest a number Between 1 - 10 \n"))
		if guest == correct_number:
			print("You're Correct")
			break
		
		else:
			print("Try Again")