import re

def check_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))  # Matches any uppercase letter
    lowercase_criteria = bool(re.search(r'[a-z]', password))  # Matches any lowercase letter
    number_cri19teria = bool(re.search(r'[0-9]', password))     # Matches any digit
    special_char_criteria = bool(re.search(r'[^\w]', password))  # Matches any special character

    # Checking the number of criteria met
    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    # Feedback based on criteria met
    if criteria_met == 5:
        feedback = "Very Strong"
    elif criteria_met == 4:
        feedback = "Strong"
    elif criteria_met == 3:
        feedback = "Moderate"
    elif criteria_met == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    # Detailed feedback
    details = {
        "Length": length_criteria,
        "Uppercase Letters": uppercase_criteria,
        "Lowercase Letters": lowercase_criteria,
        "Numbers": number_criteria,
        "Special Characters": special_char_criteria
    }

    return feedback, details

# Example usage
password = input("Enter a password to check its strength: ")
strength, details = check_password_strength(password)
print(f"Password Strength: {strength}")
print("Details:")
for criterion, met in details.items():
    print(f" - {criterion}: {'Met' if met else 'Not Met'}")