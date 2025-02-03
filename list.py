print("Create a new account.\n")
name = input("Enter username: ").capitalize()
try:
    while True:
        password = input("Enter passcode(4-Digits):")
        if len(password) <= 4 and len(password) > 3:
            break
except ValueError:
    while True:
        password = int(input("Enter passcode(4-Digits):"))
        if len(password) <= 4 and len(password) > 3:
            break

print("\nACCOUNT CREATED.\n\nLogin:")

user = input("Enter your username: ").capitalize()
passcode = int(input("Enter your passcode(4-Digits): "))

if user == name and passcode == password:
    print("Logged in")
else:
    print("Invalid Account")