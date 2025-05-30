rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    
    print("*", end="")
    
    if i > 1:
        print(" " * (2 * (i - 1) - 1), end="")
        print("*")
    else:
        print()