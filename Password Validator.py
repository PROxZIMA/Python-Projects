"""
Password Validator

A valid password is the one that conforms to the following rules:
 - Minimum length is 5;
 - Maximum length is 10;
 - Should contain at least one number;
 - Should contain at least one special character (such as &, +, @, $, #, %, etc.);
 - Should not contain spaces.

Examples:
Input: "Sololearn"
Output: false

Input: "John Doe"
Output: false

Input: "$ololearn7"
Output: true

Write a program to checks if the user input is a valid password or not.
"""
import string #imports string module

p=input('Enter the password: ')

print((4<len(p)<11) and any(x in string.digits for x in p) and any(x in string.ascii_letters for x in p) and any(x in string.punctuation for x in p) and (' ' not in p))
