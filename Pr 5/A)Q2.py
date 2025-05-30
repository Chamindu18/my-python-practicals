total = 0

for x in range (1,11):
    mark = float(input("Enter mark:"))
    total = total + mark

average = total/10
print(f"Your average is {average}")
if(average>=50):
    print("pass")
else:
    print("Fail")

