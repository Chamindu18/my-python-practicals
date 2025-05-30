print("To stop Enter -999 as Employee Number!")
count=0
while True:
    Emp_No=int(input("Enter Employee Number:"))
    if (Emp_No==-999):
        break
    Emp_Salary=float(input("Enter Employee Salary:"))
    if Emp_Salary>=5000:
        count+=1

print(f"Number of employees with salary >=5000 : {count}")
