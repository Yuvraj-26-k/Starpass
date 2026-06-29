import random

print("-" * 35)
print("STARPASS V1.1".center(35))
print("-" * 35)

special_char = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

print("What do you like to perform ?")
print("1. Password Generator")
print("2. Strength Checker")

choice = int(input("Enter your choice: "))

# ---------------- PASSWORD GENERATOR ----------------

if choice == 1:

    key = int(input("[*] Enter the length of your password: "))

    password = ""

    for i in range(key):
        password += random.choice(char)

    print("\n[*] Generated Password:", password)

# ---------------- PASSWORD CHECKER ----------------

elif choice == 2:

    password = input("Enter your password: ")

    upper = False
    lower = False
    digit = False
    special = False

    for i in password:

        if i.isupper():
            upper = True

        if i.islower():
            lower = True

        if i.isdigit():
            digit = True

        if i in special_char:
            special = True

    # Final decision AFTER the loop

    if len(password) >= 8 and upper and lower and digit and special:
       print("\n Strong Password!")

    else:
        print("\n Weak Password!")

        if len(password) < 8:
            print("[*] Password must be at least 8 characters long.")

        if not upper:
            print("[*] Password must contain at least one uppercase letter.")

        if not lower:
            print("[*] Password must contain at least one lowercase letter.")

        if not digit:
            print("[*] Password must contain at least one digit.")

        if not special:
            print("[*] Password must contain at least one special character.")

else:
    print("Invalid Choice!")

print("-" * 35)
print("THANK YOU!".center(35))
print("-" * 35)
