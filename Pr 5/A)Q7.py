number = int(input("Enter a number:"))
length = len(str(number))
original = number
armstrong_sum = 0

for i in range(length):
    digit = number%10
    armstrong_sum = armstrong_sum + digit**length
    number = number//10

if armstrong_sum==original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an armstrong number.")
    