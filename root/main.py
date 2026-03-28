import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Result
    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print(result)