#!/usr/bin/python3
print('=' * 50)
print("Starpass v1.0".upper().center(50))
print('=' * 50)

import random
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$&'
length=int(input('[*] Enter the length of your password :-'))
password=""

for i in range(length):
 password += random.choice(char)

print("[*] Generated Password :-","\n",password)
print("=" * 50)
print("Thankyou".upper().center(50))
print("=" * 50)

