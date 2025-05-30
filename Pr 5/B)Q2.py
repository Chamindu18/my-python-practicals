total=0
marks=[]
for i in range (0,10):
    mark=float(input("Enter marks of student:"))
    total+=mark
    marks.append(mark)

average=total/10
maximum=max(marks)
minimum=min(marks)

print(f"Maximum mark is:{maximum}")
print(f"Minmunm mark is:{minimum}")
print(f"Average of marks is:{average}")

