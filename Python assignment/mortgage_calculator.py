user_input = float(input("Enter Principal Amount: "))
print()
user_input2 = float(input("Enter The Annual Interest Rate: "))
print()
user_input3 = float(input("Enter Time Duration In Years: "))

DURATION_LENGTH = 12
PERCENTAGE = 100
CONSTANT = 1

rate_conversion = (user_input2 / PERCENTAGE)

proceduer1 = user_input * (rate_conversion /DURATION_LENGTH)
proceduer2 = CONSTANT + (rate_conversion /DURATION_LENGTH)
proceduer3 = (proceduer2)**(-(user_input3 * DURATION_LENGTH))
proceduer4 = CONSTANT - proceduer3 

formular = proceduer1 / proceduer4
print()
print(f"Your monthly payment is ${formular:,.2f}")
