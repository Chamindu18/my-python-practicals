base = int(input("Enter the Base:"))
exponent = int(input("Enter the exponent:"))
result = 1

for i in range (exponent):
    result = result*base

print(f"{base} into the power {exponent} is : {result}")