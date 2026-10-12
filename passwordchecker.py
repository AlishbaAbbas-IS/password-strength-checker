
import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak password"
    elif score <= 4:
        return "Medium password"
    else:
        return "Strong password"

password = input("Enter a password to check: ")
print(check_password(password))
