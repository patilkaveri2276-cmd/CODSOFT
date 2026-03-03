import secrets
import string
import sys

def get_user_preferences():
    print("\n===== PASSWORD GENERATOR =====")

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    print("\nSelect character types to include:")
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    if not any([use_lower, use_upper, use_digits, use_special]):
        print("You must select at least one character type.")
        sys.exit()

    return length, use_lower, use_upper, use_digits, use_special


def build_character_pool(use_lower, use_upper, use_digits, use_special):
    pool = ""
    guaranteed_chars = []

    if use_lower:
        pool += string.ascii_lowercase
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))

    if use_upper:
        pool += string.ascii_uppercase
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        pool += string.digits
        guaranteed_chars.append(secrets.choice(string.digits))

    if use_special:
        pool += string.punctuation
        guaranteed_chars.append(secrets.choice(string.punctuation))

    return pool, guaranteed_chars


def generate_password(length, pool, guaranteed_chars):
    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars.copy()

    for _ in range(remaining_length):
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


def save_to_file(password):
    choice = input("Do you want to save the password to a file? (y/n): ").lower()
    if choice == 'y':
        with open("generated_passwords.txt", "a") as file:
            file.write(password + "\n")
        print("Password saved to generated_passwords.txt")


def main():
    length, use_lower, use_upper, use_digits, use_special = get_user_preferences()

    pool, guaranteed_chars = build_character_pool(
        use_lower, use_upper, use_digits, use_special
    )

    password = generate_password(length, pool, guaranteed_chars)

    print("\nGenerated Secure Password:")
    print(password)

    save_to_file(password)


if __name__ == "__main__":
    main()
