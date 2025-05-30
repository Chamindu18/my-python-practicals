number = int(input("Enter a number:"))
exponent = int(input("Enter an exponent:"))
result = 1

for i in range(0,exponent):
    result = result*number
    
print(f"{number} into the power {exponent} is {result}")
