positive=0
negative=0
zero=0

for i in range(10):
    number = int(input("Enter a number:"))
    if number>0:
        positive+=1
    elif number<0:
        negative+=1
    else:
        zero+=1

print(f"Positive numbers:{positive}")
print(f"Negative numbers:{negative}")
print(f"Number of Zeros:{zero}")
    
