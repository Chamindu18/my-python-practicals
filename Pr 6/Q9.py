email = input("Enter email address:")

if "@" in email and "." in email:
    print("Email address is valid.")
else:
    print("Email address in not valid.")