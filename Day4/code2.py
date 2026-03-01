'''
Problem: Loan Approval System
Loan approved if:
Salary > 25,000
CIBIL Score > 700
if salary > 50,000 & CIBIL > 750 -> Instant Approval
Otherwise -> rejected
'''

salary = int(input("Enter Salary: "))
cibil = int(input("Enter CIBIL Score: "))
if salary > 25000 and cibil > 700:
    if salary > 50000 and cibil > 750:
        print("Instant Approval!")
    else:
        print("Loan will be approved after background verification")
else:
    print("Not Eligible")

