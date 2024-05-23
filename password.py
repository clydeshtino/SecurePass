# Copyright 2024 (Clyde Shtino)
import os
import sys
import secrets
import string
import pyperclip

def getPassword(length):
    charSet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(charSet) for i in range(length))
    return password

def repeat():
    choice = input("Would you like to generate another password? (y/n): ")

    if choice == 'y' or choice == 'Y':
       newPassword = getPassword(16)
       print("Your password has been generated successfully\n")
       print(newPassword)
       copy()
       repeat()
    elif choice == 'n' or choice == 'N':
        exit()
    else:
        print("Your input was invalid, Try again!")
        repeat()

def copy():
    copyChoice = input("Would you like to copy your password to your clipboard? (y/n): ")

    if copyChoice == 'y' or copyChoice == 'Y':
        pyperclip.copy(newPassword)
        print("Your password has been copied")
    elif copyChoice == 'n' or copyChoice == 'N':
        repeat()
    else:
        print("Your input was invalid, Try again!")
        copy()

try:
    newPassword = getPassword(16)
    print("Your password has been generated successfully\n")
    print(newPassword)
    copy()
    repeat()
except ValueError as e:
    print(f"Error : {e}")

if __name__ == '__main__':
    getPassword()     
