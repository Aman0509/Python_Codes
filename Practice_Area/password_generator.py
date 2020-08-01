#!/usr/bin/env python3

"""
This script will generate a random password for the user. Ask the user how long they want their password to be,
and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters,
as well as numbers and symbols. The password should be a minimum of 6 characters long.
"""

import random
import string
import time
import smtplib
import os

# Password parameters defined

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "{", "}", "|", "?", ";", ":"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
final_password = []

# Other Variables

msg = ["Enter desired length of password - ",
       "Enter desired count of letters - ",
       "Enter desired count of Numerals - "
       ]
temp_list = [int(input(msg[0]))]

while temp_list[0] < 6:
    print("Password length can't be less than 6!!!")
    temp_list[0] = int(input("Please enter valid password length - "))

temp_list.append(int(input(msg[1])))
while temp_list[1] > temp_list[0]:
    print("Your choice for letters length exceeds your password length")
    temp_list[1] = int(input("Please enter again the desired count of letters - "))

temp = temp_list[0]-temp_list[1]
temp_list.append(int(input(msg[2])))
while temp_list[2] > temp:
    print("Your choice for numerals length exceeds your remaining places")
    temp_list[2] = int(input("Please enter again the desired count of letters - "))

print(f"{temp-temp_list[2]} places assign for special characters")
time.sleep(0.5)
temp_list.append(temp-temp_list[2])

# Selecting the alphabets, digits and special character as per the length selected by users
final_password.extend(random.sample(string.ascii_letters, temp_list[1]))
final_password.extend(random.sample(digits, temp_list[2]))
final_password.extend(random.sample(special_characters, temp_list[3]))

# Randomly Shuffling List
random.shuffle(final_password)

# Printing the Final Password and also sending mail to the user
print("\nGenerated Password is '{}'".format(''.join(final_password)))

# Creating SMTP session
with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.ehlo()
    s.starttls()
    s.ehlo()
    receiver_mail_id = input("Enter receiver's mail id - ")
    user_id = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    s.login(user_id, password)
    subject = "Confidential: New Password Generated"
    body = "Generated Password is '{}'".format(''.join(final_password))
    s.sendmail(user_id, receiver_mail_id, f"Subject: {subject}\n\n{body}")
    print("Password Sent Successfully!!")
