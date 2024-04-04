price =float(input("Enter price \n"))
discount =float(input("Enter discount \n"))

PERCENT_DISCOUNT = 100

print("The price after discount is:" + 
 str(price -((price * discount)/PERCENT_DISCOUNT )) +"\n")