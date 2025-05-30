total = 0
while True:
    number=int(input("Enter a number:"))
    if number == -1:
        break
    total+=number
print(f"the total is {total}")
