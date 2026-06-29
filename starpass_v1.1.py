#!/usr/bin/python3
import random
print('=' * 50)
print("Starpass v1.1".upper().center(50))
print('=' * 50)

print("What would you like to perform ?")
print("1.Password Generator")
print("2.Strength Checker")

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$&'
special_char="!@#$^&(){}[]?"

choice=int(input("Enter your choice:-"))

if choice == 1:

#---------PASSWORD GENERATOR----------

 pass1=int(input('[*] Enter the length of your password :-'))
 password=""

 for i in range(pass1):
  password += random.choice(char)


 print("[*] Generated Password:","\n",password)


elif choice == 2:

#--------STRENGTH CHECKER--------

 pass2=str(input("Enter your password:-"))

 upper=False
 digit=False
 special=False

 for i in pass2:
  if i.isupper():
    upper = True
  if i.isdigit():
    digit = True
  if i in special_char:
    special = True
  if len(pass2) >= 8 and upper and digit and special:
    print("Strong password")
  else:
    print("Wrong password!")
    if len(pass2) < 8:
     print("[*] Password must be 8 characters long")
    if not upper:
     print("[*] Password must contain atleast one uppercase letter")
    if not digit:
     print("[*] Password must contain atleast one digit")
    if not special:
     print("[*] Password must contain atleast one special character","\n","like:-",special_char)
else:
 print("Invalid choice")
 print("-"*50)
 print("Thank you".center(50).upper())
 print("-"*50)





















