num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if (num2 == 0):
    print("Can't divide by zero.")
elif(num1%num2 == 0):
    print("The first number is a multiple of the second number.")
else:
    print("The first number is not a multiple of the second number.")
    
