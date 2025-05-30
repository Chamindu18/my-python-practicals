operator = input("Chose an operator[+,-,*,/]:")
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

if(operator == "+"):
    print(f"The sum of numbers is : {number1 + number2}")
elif(operator == "-"):
    print(f"The difference of numbers is : {number1 - number2}")
elif(operator == "*"):
    print(f"The product of numbers is : {number1 * number2}")
elif(operator == "/"):
    print(f"The division of numbers is : {number1/number2}")
else:
    print("Invalid Operator.")
