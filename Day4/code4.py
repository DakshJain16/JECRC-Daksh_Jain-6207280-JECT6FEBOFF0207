'''WAP to take a character and convert lowercase to uppercase and vice-versa'''
# ch = input("Enter a character: ")
# if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
#     if ord(ch) >= 97 and ord(ch) <= 122:
#         ch = ord(ch) - 32
#         print(f"Uppercase character: {chr(ch)}")
#     else:
#         ch = ord(ch) + 32
#         print(f"Lowercase character: {chr(ch)}")
# else:
#     print(ch)

ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print(chr(ord(ch) + 32))
elif 'a' <= ch <= 'z':
    print(chr(ord(ch) - 32))
else:
    print(ch)