# SecurePassword 
# By: Clyde Shtino 

## About
SecurePassword is a simple python script that will generate a secure password cryptographically. The script also offers functionality such as copying the password to clipboard and keep repeating the process (utilizing recursion) to generate as many passwords as the user wishes

## Libraries Required
secrets: For generating cryptographic random integers, letters, and symbols (pip/pip3 install secrets)

string: To use string constraints (pip/pip3 install string)

pyperclip: For copying password functionality (pip/pip3 install pyperclip)

## getPassword()
The getPassword function generates a random password of 16 characters (fixed integer argument in function call). It uses a combination of of ASCII letters, numbers, and punctuation characters. As a result a password is returned

## repeat()
Repeat function prompts the user whether they want to generate a another password or not.

## copy()
Copy function copies the password based on the user input



