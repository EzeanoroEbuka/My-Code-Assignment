number = int(input("Enter Number: "))
count = 1
factoria  = 1
while(number >= count):
	factoria *= count
	count = count + 1
print(factoria)  