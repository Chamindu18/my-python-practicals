numbers = []

def evennumber():
    n = int(input("How many numbers do you want to enter? :"))
    for i in range (n):
        number = int(input("Enter a number:"))
        numbers.append(number)
    for i in numbers:
        if i % 2 == 0:
            print(f"{i} is EVEN.")
        else:
            print(f"{i} is ODD.")

evennumber()