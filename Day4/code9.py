'''
Achieve the desired output
INPUT : {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
OUTPUT : {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
'''

# Solution 2
coll = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
new_coll = {}
for i in coll:
    new_coll[coll[i]] = i
print(new_coll)
