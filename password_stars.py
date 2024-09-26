"""Password length w/ error checking"""

PASSWORD_LENGTH = 4

password = input("Enter a password: ")
while len(password) < PASSWORD_LENGTH:
    print(f"Password needs to be at least {PASSWORD_LENGTH} characters long.")
    password = input("Enter a password: ")

print("*" * len(password))
