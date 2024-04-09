score = int(input(" Enter Score \n"))

MAX_MARK = 100

if score >= 80 and score <= MAX_MARK:
	print(f"your score is {score:} and your Grade is A")
elif score >= 65 and  score <= 79:
	print(f"your score is {score:} and your Grade is B")
elif score >= 50 and score <= 64:
	print(f"your score is {score:} and your Grade is C")
elif score >= 40 and score <= 49:
	print(f"your score is {score:} and your Grade is D")
elif score > MAX_MARK:
	print("YOU BE OLE")
else :
	print("FAILED")