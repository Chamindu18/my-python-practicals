number = int(input("Enter a number:"))
Digit_sum = 0
while(number > 0):
    Digit_sum = Digit_sum + number%10
    number = number//10

print(f"The sum of digits is : {Digit_sum}")



 