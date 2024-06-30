import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate password
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Change this to your desired length
    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")
