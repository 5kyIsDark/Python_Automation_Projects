import string

print("-----------------------------")
print("  Password Strength Checker  ")
print("-----------------------------")

password = input("Please Enter Your Password: ").strip()
score = 0
special = string.punctuation

if not password:
    print("❌ Password cannot be empty!")
    exit()

if len(password) >= 8:
    score+=2.5
else:
    print("Your password can be stronger with more than 8 characters...")

if any(char.isupper() for char in password) and any(char.islower() for char in password):
    score+=2.5
else:
    print("Your Password Can Be Stronger with Both lower and upper case charcter...")

if any(char.isdigit() for char in password):
    score+=2.5
else:
    print("You Password Could Be stronger with digits...")

if any(char in special for char in password):
    score+=2.5
else:
    print("Your Password could be stronger with special character...")


if score == 10:
    strength = "Strong 💪"
elif score >= 7.5:
    strength = "Moderate 🔐"
else:
    strength = "Weak ❌"

print(f"Password Score --> {int(score)}/10 ({strength})")
