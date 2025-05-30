num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print(f"Before swap : First number = {num1} & Second number = {num2}")

num1, num2 = num2, num1

print(f"After swap : First number = {num1} & Second number = {num2}")
