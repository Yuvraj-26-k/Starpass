# 🔐 StarPass v1.1

A simple Python-based password utility that allows users to generate secure passwords and check the strength of existing passwords.

---

## ✨ Features

- 🔑 Random Password Generator
- 🛡️ Password Strength Checker
- ✔ Checks for:
  - Minimum length (8+ characters)
  - Uppercase letters
  - Numbers
  - Special characters
- 🖥️ Easy-to-use command-line interface

---

## 📸 Preview

```
==================================================
                  STARPASS V1.1
==================================================

1. Password Generator
2. Strength Checker

Enter your choice:
```

---

## 🛠️ Technologies Used

- Python 3
- Random Module

---

## 📂 Project Structure

```
StarPass/
│
├── starpass.py
├── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Yuvraj-26-k/StarPass.git
```

Move into the project folder:

```bash
cd StarPass
```

Run the program:

```bash
python3 starpass.py
```

---

## 🔑 Password Generator

Generates a random password based on the length entered by the user.

Example:

```
Enter password length: 12

Generated Password:
aD7#fL2@qP9!
```

---

## 🛡️ Password Strength Checker

Checks whether a password contains:

- Minimum 8 characters
- Uppercase letter
- Number
- Special character

Example:

```
Password: MyPass@123

Result:
Strong Password
```

If the password is weak, the program explains what is missing.

Example:

```
Password must be at least 8 characters.
Password must contain at least one uppercase letter.
Password must contain at least one special character.
```

---

## 🎯 Future Improvements

- Password History
- Password Entropy Calculator
- Save Passwords to File
- Clipboard Support
- Colorful Terminal Output
- GUI Version (Tkinter / CustomTkinter)

---

## 👨‍💻 Author

**Yuvraj Singh**

Cybersecurity | Python | Linux | Networking | Arduino

---
