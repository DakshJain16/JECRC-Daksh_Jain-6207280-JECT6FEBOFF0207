import csv
from datetime import date

file = open('expense.csv', 'a+')
# w = csv.writer(file)
r = csv.reader(file)
file.seek(0)
print(list(r))

# w.writerow(['DATE', 'CATEGORY', 'AMOUNT'])  ## to provide column names
# w.writerows(  ## to provide data
#     [
#         [date.today(), 'Travel', 2000],
#         [date.today(), 'Food', 550],
#         [date.today(), 'Entertainment', 1700]
#     ]
# )

file.close()