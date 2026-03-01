'''
INPUT : ('Hello', 'Hi', 20, 40.2, 9.6j, [1, 2], 'PYTHON', 'JECRC', (1,2,3))   
OUTPUT : {'Hello' : 'l', 'Hi' : 'Hi', 'PYTHON' : 'PN', 'JECRC' : 'C'}
'''

# coll = ('Hello', 'Hi', 20, 40.2, 9.6j, [1, 2], 'PYTHON', 'JECRC', (1,2,3))
# coll = eval(input('Enter a collection: '))
# new_coll = {}
# for i in coll:
#     if type(i) in [str, tuple]:
#         if len(i) % 2 != 0:
#             new_coll[i] = i[len(i) // 2]
#         else:
#             new_coll[i] = i[0] + i[- 1]

# print(new_coll)

coll = [1, 1.2, 3, 4, 5, 'HI']
i, flag = coll[0], True

for j in coll:
    if type(i) != type(j):
        flag = False
        break
if flag:
    print('Homogeneous Collection')
else:
    print('Heterogeneous Collection')