# import libraries
import random
import string


# Function for user input for how long the password is got to be between 8 and 15 characters
def password_gen():
    while True:
        password_length = int(input("How long does your password need to be (between 8 and 15 characters)? "))
        if password_length in range(8, 16):
            # Creating a random password from imported libraries
            password_characters = string.ascii_letters + string.digits + string.punctuation

            # Password string entry

            password = []

            # Adding 2 uppercase characters to the string
            password.append(random.choice(string.ascii_letters).upper())
            password.append(random.choice(string.ascii_letters).upper())

            # Adding 2 number characters to the string

            password.append(random.choice(string.digits))
            password.append(random.choice(string.digits))

            # Using user input for adding the right amount of characters for password

            for x in range(password_length - 4):
                password.append(random.choice(password_characters))

            # Shuffle characters so they are not in order

            random.shuffle(password)

            # print password
            print("Your random password is", "".join(password))
            break

        # If the user makes a mistake and enters an amount that is not in between 8 and 15 goes back to ask how long the password is required

        if password_length not in range(8, 16):
            print("Please make a valid selection")


# Welcome to the password generator

print("Welcome to the Password Generator")

# Menu

while True:
    print("Menu")
    print("1: To generate a password between 8 and 15 characters")
    print("e: To exit.")

    # User Choice

    menu = input("Please enter your choice >")

    if menu == "1":
        (password_gen())

    if menu == "e":
        break
print("Thank you for using Password Generator")
print("Goodbye")

# End of Program
