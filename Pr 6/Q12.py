while True:
    password = input("Enter a Password:")
    if len(password)>=8:
        print("New password Accepted.")
        break
    else:
        print("Password must be at least 8 characters.")
        
        
