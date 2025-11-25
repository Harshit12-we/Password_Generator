import random
import string

def generate_password(length):
    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


# Main program
print("Password Generator")
length = int(input("Enter the desired password length: "))

password = generate_password(length)
print("Your generated password is:", password)
