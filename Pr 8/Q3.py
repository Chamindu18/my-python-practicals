def seconds_12(h,m,s):
    if h == 12:
        h = 0
    total_seconds = h*3600 + m*60 + s
    return total_seconds

h1 = int(input("Enter 1st Hour(1-12):"))
m1 = int(input("Enter 1st Minute(0-59):"))
s1 = int(input("Enter 1st Second(0-59):"))

h2 = int(input("Enter 2nd Hour(1-12):"))
m2 = int(input("Enter 2nd Minute(0-59):"))
s2 = int(input("Enter 2nd Second(0-59):"))

t1 = seconds_12(h1,m1,s1)
t2 = seconds_12(h2,m2,s2)

difference = abs(t1 - t2)

print(f"Seconds since the clock stuck 12 o'clock for First Time : {t1} seconds")
print(f"Seconds since the clock stuck 12 o'clock for Second Time : {t2} seconds")
print(f"Difference between the two times : {difference} seconds")