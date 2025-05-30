numbers=[]
even=0
odd=0
for i in range (0,10):
    num=int(input(f"Enter number {i+1}:"))
    if num&2==0:
        even+=1
    else:
        odd+=1
    numbers.append(num)
    #append(num)= adds the number to the list
print(f"Number of Even numbers:{even}")
print(f"Number of Odd numbers:{odd}")
print(f"The array is {numbers}")