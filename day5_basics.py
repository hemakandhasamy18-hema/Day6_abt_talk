# Login System

correct_username = "hema"
correct_password = "12345"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome", username)
        break
    else:
        attempts -= 1
        print("Invalid username or password.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Account locked! Too many failed attempts.")