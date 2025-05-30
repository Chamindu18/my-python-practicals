num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1>num2 and num1>num3):
    largest = num1
elif(num2>num1 and num2>num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")

if(num1<num2 and num1 <num3):
    smallest = num1
elif(num2<num1 and num2<num3):
    samllest = num2
else:
    smallest = num3

print(f"The smallest number is {smallest}")
