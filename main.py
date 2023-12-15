import secrets
import string

def generate_password(length):
    characters = string.printable.strip()
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

while True:
    length = input("Enter the length of the password: ")
    try:
        length = int(length)
        print(generate_password(length))
    except ValueError:
        print("Please enter a valid number.")




    