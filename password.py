import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ""

    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        print("Error: Please select at least one character set.")
        return None

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

    use_letters = input("Include letters (yes/no)? ").lower() == 'yes'
    use_numbers = input("Include numbers (yes/no)? ").lower() == 'yes'
    use_symbols = input("Include symbols (yes/no)? ").lower() == 'yes'

    return length, use_letters, use_numbers, use_symbols

if __name__ == "__main__":
    print("Password Generator")
    user_input = get_user_input()

    if user_input:
        length, use_letters, use_numbers, use_symbols = user_input
        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print("\nGenerated Password:", password)