# 🔐 Password Strength Checker (Python Automation)

This simple Python script checks how strong a password is by analyzing its length, character variety, and complexity.

It provides feedback and a score out of 10, helping users create more secure passwords.

---

## ✅ Features

- Checks for:
  - Minimum length of 8 characters
  - Use of both uppercase and lowercase letters
  - At least one digit
  - At least one special character (`!@#$%`, etc.)
- Prevents empty password input
- Gives a total score and strength label:
  - `Strong 💪`
  - `Moderate 🔐`
  - `Weak ❌`
- Offers feedback on what’s missing

---

## 🧰 Requirements

- Python 3.x  
- No external libraries required

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python password_checker.py
   ```

2. Enter a password when prompted.

3. You'll see a breakdown of what your password passed/failed and a final score like:

   ```
   Password Score --> 10/10 (Strong 💪)
   ```

---

## 📁 Example

**Input:**
```
Enter password: Python@123
```

**Output:**
```
Password Score --> 10/10 (Strong 💪)
```

---

## 📦 File Structure

```
password_checker.py
README.md
```

---

## 🛡 License

This project is licensed under the MIT License.
