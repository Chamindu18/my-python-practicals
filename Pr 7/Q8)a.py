def findhypo(side1,side2):
    hypotenuse = (side1**2 + side2**2)**(1/2)
    return hypotenuse

n1 = float(input("Enter value of Side 1:"))
n2 = float(input("Enter value of Side 2:"))
print(f"The Hypotenuse is : {round(findhypo(n1,n2),2)}")

