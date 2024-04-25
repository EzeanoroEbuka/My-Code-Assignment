WINNING_NUMBER = 8
for number in range(1,4):
	guest = int(input("Guest a number Between 1 - 10 \n"))

	if guest == WINNING_NUMBER:
		print("You're Correct")
		break
		
	else:
		print("Try Again")
	