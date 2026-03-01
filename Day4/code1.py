'''
Problem 1: Calculate electricity bill based on the units consumed.
0-100 -> ₹5/unit
101-300 -> ₹7/unit
above 300 -> ₹10/unit
if bill > 500 -> 5% discount
'''

# unit = int(input("Enter the units consumed: "))
# if unit > 0:
#     if unit <= 100:
#         bill = unit * 5 
#     elif unit <= 300:
#         bill = (100 * 5) + (unit - 100) * 7
#     else:
#         bill = (100 * 5) + (200 * 7) + (unit - 300) * 10

#     if(bill > 5000):
#         bill = bill * 0.95
#     print(f'The bill amount is: {bill}')
# else:
#     print("Enter valid inputs!")


unit = int(input("Enter the units consumed: "))
bill = None
if unit > 0:
    if unit <= 100:
        bill = unit * 5 
    elif 101 <= unit <= 300:
        bill = unit * 7
    else:
        bill = unit * 10

    if(bill > 5000):
        bill = bill * 0.95

    print(f'The bill amount is: {bill}')
else:
    print("Enter valid inputs!")

