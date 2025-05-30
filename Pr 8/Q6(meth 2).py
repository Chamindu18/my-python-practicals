def digit_reverse(num):
    rev = str(num)[::-1]
    return int(rev)

n = int(input("Enter a number series:"))
print(f"The reversed number : {digit_reverse(n)}")