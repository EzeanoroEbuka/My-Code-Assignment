total = 0
miles_per_gallon = 0
gallons = 0
count = 0
while gallons != -1:

	gallons = float(input("Enter Gallons used (-1 to end): "))
	if(gallons == -1):
		break
	miles = float(input("Enter Miles Drive: "))

	miles_per_gallon = miles / gallons 
	total += miles_per_gallon
	count = count + 1
	print(f"The miles/ gallon for this tank was {miles_per_gallon:.5f}")

average = total / count

print(f"The Overall Average mile/gallon was {average:.5f}")