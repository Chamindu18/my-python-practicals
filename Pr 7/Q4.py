def finddivision(a,b):
    if b==0:
        return "Can't Divide by ZERO."
    else:
        return (a/b)

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
print(f"The Quotient of two numbers : {finddivision(n1,n2)}")