import random
import string

def generate_password(length: int) -> str:
    """
    Generates a random password of a specified length and complexity.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A randomly generated password.
    """
    if length <= 0:
        return "Password length must be a positive number."

    # Define the sets of characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to generate a list of random characters and then join them into a string
    password_list = random.choices(characters, k=length)
    password = "".join(password_list)

    return password

def main():
    """
    Main function to handle user input and display the generated password.
    """
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired length for your password: "))

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Your generated password is:", password)

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
