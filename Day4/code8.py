'''
#WAP to find out the maximum number 
INPUT : [10, 2.2, 5, 'Hello', [100, 200], 99.9]
OUTPUT : 99.9
'''

l1 = [10, 2.2, 5, 'Hello', [100, 200], 99.9]
max1 = 0
for i in l1:
    if type(i) in [int, float]:
        if max1 <= i:
            max1 = i

print(max1)
