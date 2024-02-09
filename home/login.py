def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == "dev" and password == "securepassword":
            print("Login successful")
            break
        else:
            print("Try again")

login()