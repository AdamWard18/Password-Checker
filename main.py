import re

def check_password_strength(password):
   common_passwords = {
       "password", "123456", "123456789", "qwerty",
       "abc123", "letmein", "welcome", "monkey",
       "login", "admin"
   }
   sequences = ["abc", "123", "abcd", "1234", "qwerty", "12345", "abcdef"]

   checks = {
       "length": len(password) >= 12,
       "uppercase": any(c.isupper() for c in password),
       "lowercase": any(c.islower() for c in password),
       "digit": any(c.isdigit() for c in password),
       "special": any(not c.isalnum() for c in password),
       "not_common": not any(common in password.lower() for common in common_passwords),
       "no_repeats": not re.search(r'(.)\1{2,}', password),
       "no_sequences": not any(seq in password.lower() for seq in sequences)
   }

   problems = []
   if not checks["length"]:
       problems.append("Password should be at least 12 characters long.")
   if not checks["uppercase"]:
       problems.append("Include at least one uppercase letter.")
   if not checks["lowercase"]:
       problems.append("Include at least one lowercase letter.")
   if not checks["digit"]:
       problems.append("Include at least one digit.")
   if not checks["special"]:
       problems.append("Include at least one special character.")
   if not checks["not_common"]:
       problems.append("Password is too common or easily guessable.")
   if not checks["no_repeats"]:
       problems.append("Avoid repeating the same character multiple times.")
   if not checks["no_sequences"]:
       problems.append("Avoid common sequences like '1234' or 'abcd'.")

   score = sum(checks.values())

   if problems:
       print("Password Strength Issues:")
       for p in problems:
           print(f"- {p}")

   ratings = {
       8: "Outstanding",
       7: "Excellent",
       6: "Very Strong",
       5: "Strong",
       4: "Good",
       3: "Moderate",
       2: "Weak",
       1: "Very Weak",
       0: "Super Weak"
   }

   return ratings[score], score


password = input("Enter your password: ")
strength, score = check_password_strength(password)
print(f"Password strength: {strength} ({score}/8)")