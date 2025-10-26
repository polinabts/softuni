def len_password(some_password: str) -> str or None:
    if len(some_password) < 6 or len(some_password) > 10:
        return "Password must be between 6 and 10 characters"


def letters_password(some_password: str) -> str or None:
    if not some_password.isalnum():
        return "Password must consist only of letters and digits"

def digits_password(some_password: str) -> str or None:
    digits_counter = 0
    for current_character in some_password:
        if current_character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        return "Password must have at least 2 digits"


password = input()

error_message =len_password(password), letters_password(password), digits_password(password)

len_check = len_password(password)
letter_check = letters_password(password)
digits_check = digits_password(password)

if len_check is None and letter_check is None and digits_check is None:
    print("Password is valid")
else:
    for msg in (len_check, letter_check, digits_check):
        if msg:
            print(msg)
