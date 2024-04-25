num1 = float(input("Enter Coefficients of x2 \n"))
num2 = float(input("Enter Coefficients of x \n"))
num3 = float(input("Enter Intercept \n"))

CONSTANT1 = -4
CONSTANT2 = 2

discriminant = ((num2**2)+ (CONSTANT1 * num1 * num3))** 0.5

divisor = (CONSTANT2 * num1)

negative_value = (-num2 - discriminant) / divisor
positive_value = (-num2 + discriminant) / divisor 

print(f"The value of x are:\nx = {positive_value:.4f} or \nx = {negative_value:.4f}")

