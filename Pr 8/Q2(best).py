def even(number):
    if number % 2 == 0:
        return 1
    else:
        return 0

n = int(input("How many numbers do you want to enter?:"))
numbers = []

for i in range (n):
    num = int(input("Enter a number:"))
    numbers.append(num)

for i in numbers:
    if even(i) == i:
        print(f"{i} is EVEN.")
    else:
        print(f"{i} is ODD.")
    