import re

def check_password_strength(password):
    length = len(password) >= 30
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    number = any(char.isdigit() for char in password)
    special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    score = sum([length, upper, lower, number, special])
    
    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength[score], "Consider adding more complexity!" if score < 3 else "Your password is secure."

password = input("Enter your password: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}\nFeedback: {feedback}")
