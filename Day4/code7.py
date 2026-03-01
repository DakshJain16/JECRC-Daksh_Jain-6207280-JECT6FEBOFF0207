'''achieve the desired output for the below given input
INPUT : RAhul@123Gh
OUTPUT : raHUL@123gH
Restriction : you can't use any in-built functions'''

inp = input("Enter input: ")
res = ''
for i in inp:
    if 'A' <= i <= 'Z':
        res += chr(ord(i) + 32)
    elif 'a' <= i <= 'z':
        res += chr(ord(i) - 32)
    else:
        res += i

print(res)