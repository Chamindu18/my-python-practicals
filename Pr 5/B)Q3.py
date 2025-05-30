great=0
total=0
for i in range(0,10):
    price=float(input("Enter price of item:"))
    total+=price
    if price>200:
        great+=1

average=total/10

print(f"Average value of an item:{average}")
print(f"Number of items price greater than 200:{great}")