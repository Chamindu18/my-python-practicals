def average(avg):
    if avg<0 or avg>100:
        return "Invalid Average"
    elif avg<60:
        return 0
    elif avg<=69:
        return 1
    elif avg<=79:
        return 2
    elif avg<=89:
        return 3
    elif avg<=100:
        return 4
    
n = float(input("Enter the average:"))
print(f"Students Quality point :{average(n)}")