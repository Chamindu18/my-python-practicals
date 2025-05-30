def findmin(a,b,c):
    if a<b and a<c:
        m = a
    elif b<a and b<c:
        m = b
    else:
        m = c
    return m

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))
print(f"The smallest number is : {findmin(n1,n2,n3)}")