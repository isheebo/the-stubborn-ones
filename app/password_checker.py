"""
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

1. At least 1 letter between [a-z]

2. At least 1 number between [0-9]

3. At least 1 letter between [A-Z]

4. At least 1 character from [$#@]

5. Minimum length of transaction password: 6

6. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will

check them according to the above criteria. Passwords that match the criteria
are to be printed, each separated by a comma
"""

import re


def is_valid_password(password):
    return re.match(
        "^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$",
        password
    ) is not None


def parse_input(passwords):
    return passwords.split(",")


def valid_passwords(passwords):
    valid_pwds = []
    passwords = parse_input(passwords)

    for password in passwords:
        if is_valid_password(password.strip()):
            valid_pwds.append(password)
    return valid_pwds


def display_valid_passwords(passwords):
    pwds = valid_passwords(passwords)
    return ", ".join(pwds) if pwds else "None of the passwords is valid"
