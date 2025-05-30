operator = input("Enter what you want to calculate[circumference,volume,area]:")
radius = float(input("Enter the radius:"))
if(operator == 'circumfernce'):
    print(f"The circumference of the circle is : {2*(22/7)*radius}")
elif((operator == 'volume')):
    print(f"The volume of the circle is : {(4/3)*(22/7)*radius**3}")
elif(operator == 'area'):
    print(f"The area of the circle is : {(22/7)*radius**2}")
else:
    print("Invalid input.")
    