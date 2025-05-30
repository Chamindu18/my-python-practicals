numbers = []
for i in range(10):
    number = int(input(f"Enter number {i+1}:"))
    numbers.append(number)
highest = max(numbers)
lowest = min(numbers)

print(f"The maximum nuber is : {highest}")
print(f"The minimum number is :{lowest}")