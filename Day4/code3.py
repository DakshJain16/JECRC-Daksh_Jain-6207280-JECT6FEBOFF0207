'''
Problem: WAP to check whether a year is leap year or not
'''

year = int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")


