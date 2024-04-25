import math
calculated_value = 0

def area_of_circle(radius):
	calculated_value = math.pi * (radius **2)
	
	return (f"{calculated_value:.2f}")

print("The Area Of The Circle is: " + area_of_circle(7))