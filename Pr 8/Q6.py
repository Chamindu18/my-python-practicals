def digit_reverse():
    num = int(input("Enter a number(least 2):"))
    numstr = str(num)
    rev = numstr[::-1]
    numint = int(rev)
    return numint

print(f"The reverse number : {digit_reverse()}")


