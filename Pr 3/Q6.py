name = input("Enter the salesmen name:")
Syear = int(input("Enter the number of service years:"))
Bsalary = float(input("Enter the basic salary:"))
city = input("Enter 'C' if the city is Colombo, If not type the city name:")
bonus = 0
allowance = 0
increment = 0

if(Syear>=5):
    bonus = Bsalary*0.1
if(city.lower() == 'c'):
    allowance = 2500
if(Bsalary<25000):
    increment = Bsalary*0.1
elif(25000<=Bsalary and Bsalary<50000):
    increment = Bsalary*0.12
else:
    increment = Bsalary*0.15

Nsalary = Bsalary + bonus + allowance + increment

print(f"Salesmen name: {name}")
print(f"Gross monthly remuneration of salesman: {Nsalary}")


