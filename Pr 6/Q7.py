password = input("Enter the Encoded Password:")
newpass = ""
for i in password:
    code = str(ord(i))
    newpass+=code

print(f"The password is : {newpass}")

