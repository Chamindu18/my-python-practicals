name = input("Enter employee name:")
Bsalary = float(input("Enter the basic salary:"))

if(Bsalary<5000):
    increment = Bsalary*0.05
elif(Bsalary>=5000 and Bsalary<10000):
    increment = Bsalary*0.1
else:
    increment = Bsalary*0.15

Nsalary = Bsalary + increment

print(f"Employee name is {name} and new salary is {Nsalary}")
