RANGES = 15
PASS_MARK = 45
passed = 0
failed = 0
for scores in range (0,RANGES):
	score = int(input("Enter Score \n"))
	if score >= PASS_MARK:
		passed = passed + 1
	if score < PASS_MARK:
		failed = failed + 1
	

print(f"Total passed Students are {passed} \nTotal failed student are {failed}")