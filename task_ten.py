principal = float(input("Enter Amount To be invested \n"))
years = int(input("Enter years \n")) 

RATE = 5
PERCENT = 100
annual_rate = RATE / PERCENT
rate_in_years = 1
compound_amount = 0
for year in range(years):
	amount = principal * (1 + annual_rate) ** years
	compound_amount += amount

print(f"The amount on deposit at the end of the nth year is: {compound_amount:,.2f}")