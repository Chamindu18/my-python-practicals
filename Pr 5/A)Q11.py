number = int(input("Enter a number:"))
if number <= 0 :
    print("Number should be greater than zero.")
else:
    print(f"The factors of {number} are:")
    for i in range(1,number+1):
        if number%i==0:
            print(i)