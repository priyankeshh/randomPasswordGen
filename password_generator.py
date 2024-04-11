import random
import string

def generate_password(length, include_capitals=False, include_special_chars=False, include_numbers=False):
    characters = string.ascii_lowercase
    if include_capitals:
        characters += string.ascii_uppercase
    if include_special_chars:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input(prompt):
    user_input = input(prompt).lower()
    return user_input == "y"


length = int(input("Enter the length of the password: "))
include_capitals = get_user_input("Include capital letters? (y/n): ")
include_special_chars = get_user_input("Include special characters? (y/n): ")
include_numbers = get_user_input("Include numbers? (y/n): ")

password = generate_password(length, include_capitals, include_special_chars, include_numbers)
print("Generated password:", password)

