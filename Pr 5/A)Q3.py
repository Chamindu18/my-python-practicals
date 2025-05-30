number = int(input("Enter a number:"))
factorial = 1
while(number>0):
    if(number == 0):
        factorial = 1
    else:
        factorial = factorial * number
        number = number - 1
print(f"The factorial of the number is : {factorial}")
