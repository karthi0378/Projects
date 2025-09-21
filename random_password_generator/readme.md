# 🔑 Password Generator

This is a simple **Python-based password generator** that creates strong, customizable passwords based on user preferences.

## 🚀 Features
- Choose the **password length**.
- Option to include:
  - ✅ Uppercase letters
  - ✅ Special characters
  - ✅ Digits
- Ensures at least one character from each selected type.
- Shuffles characters for better randomness.

## 📂 Code Overview
The program:
1. Collects user preferences:
   - Password length
   - Whether to include uppercase letters
   - Whether to include special characters
   - Whether to include digits
2. Builds a character pool using Python's built-in `string` module.
3. Ensures all selected character types appear at least once.
4. Randomly generates a password and shuffles it.
5. Prints the final password.

## 🛠️ Usage
Run the script in your terminal:

```bash
python password_generator.py
