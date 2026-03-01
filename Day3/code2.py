## elif statement
## when you have multiple conditions; multiple statement blocks;
## atleast one if condition should be there.

## WAP in python to take a character from the user and check whether it is a vowel
## or consonant, digit or special character
'''
1. Take a character from the user.
2. Apply the conditions one by one'''

ch = input("Enter a character: ")
if ch in 'aeiouAEIOU':
    print('Vowel!')
elif ch in '0123456789':
    print('Digit!')
elif (ch >= 'a' or ch <= 'z' or ch >= 'A' or ch <= 'Z') and ch not in 'aeiouAEIOU':
    print('Consonant!')
else:
    print('Special Character!')