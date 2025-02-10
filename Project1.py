import re
import random
import string

def check_password_strength(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[@$!%*?&#]', password))
    }
    
    score = sum(criteria.values())
    
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

if __name__ == "__main__":
    print("# Developed by Saif at ShulaTech Solutions Cyber Security Internship  ")
    user_password = input("Enter a password to check its strength: ")
    strength = check_password_strength(user_password)
   
    print(f"Password Strength: {strength}")
    
    if strength != "Strong":
        print("Consider using a stronger password. Here's a suggestion:")
        print(generate_strong_password())