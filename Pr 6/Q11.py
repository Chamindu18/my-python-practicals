students = []

for i in range (5):
    name = input(f"Enter the name of student {i+1}:")
    students.append(name)

students.sort()

print(f"The first student : {students[0]}")
print(f"The last syudent : {students[-1]}")