# Functions for String Data Type
'''
1. lower
2. upper
3. capitalize
4. title
5. strip
6. lstrip
7. rstrip
8. replace
9. index
10. split
11. join
12. startswith
13. endswith
14. isdigit
15. isalpha
16. islower
17. isupper'''

s = 'Python123'
print(s.lower()) ## return value
res = s.upper()
print(res)

s1 = 'pyTHon'
print(s1.capitalize())

para = "today is thursday."
print(para.title())

print(' JECRC '.strip())
print('JECRC'.strip('C'))
print('  JECRC'.lstrip())
print('python'.lstrip('p'))
print('  JECRC  '.rstrip())
print('python'.rstrip('n'))

s2 = 'JECRC'
print(s2.replace('C', 'c'))

print('python'.index('t'))
print('python'.find('a'))

s3 = 'I LOVE PYTHON PROGRAMMING LANGUAGE'
print(s3.split())
print(s3.split('PYTHON'))
s3 = 'I-LOVE-PYTHON-PROGRAMMING-LANGUAGE'
print(s3.split('-'))

list_of_strs = ['I', 'LOVE', 'PYTHON', 'PROGRAMMING', 'LANGUAGE']
'''
join(self, iterable, /) unbound builtins.str method
    Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.

    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
'''
print(' '.join(list_of_strs))
print('-'.join(list_of_strs))
print('@'.join(list_of_strs))

s4 = 'python'
print(s4.startswith('p'))
print(s4.startswith('t', 2))
print(s4.startswith('t', 2, 4))
print(s4.endswith('n'))
print(s4.endswith('n', 1))
print(s4.endswith('n', 1, 4))

s5 = '1234'
print(s5.isdigit())

s5 = 'abc'
print(s5.isalpha())

print(s5.islower())

s5 = 'ABC'
print(s5.isupper())

# Functions of List Data Type 
'''
1. append
2. insert
3. extend
4. pop
5. remove
6. clear
7. sort
8. reverse
9. index
10. count
'''

l1 = [10, 20, 30]
l1.append(40)
print(l1)

l1.insert(2, 50) # --> if index not present, inserts at last
print(l1)

l1.extend([60, 70, 80])
print(l1)

l1.pop()
print(l1)
# l1.pop(8) --> IndexError: pop index out of range
l1.pop(2)
print(l1)

l1.remove(40)
print(l1)

l2 = [2, 71, 50, 47, 29]
l2.sort()  #---> ascending
print(l2)
l2.sort(reverse = True)  # ---> descending
print(l2)

l2 = [1, 2, 0.5, 1]
l2.reverse()  #---> never sorts the list, just reverses it
print(l2)

print(l2.index(50))

l3 = [1, 2, 3, 5, 1, 5, 4, 3, 2, 1]
print(l3.count(1)) #---> count the number of occurrances of data item
print(l3.count(5))

l2.clear()  #---> empties the list, but retains structure 
print(l2)


# Functions for Tuple Data Type
'''
1. index
2. count
'''

tup = (10, 20, 50, 40, 40, 10, 20, 30)
print(tup.index(50))
print(tup.count(40))

# Functions for Set Data Type
'''
1. add
2. remove
3. discard
4. pop: randomly eliminates the values, single value at a time
5. clear    ---> empties the set but structure remains intact
6. union
7. intersection
8. difference
10. symmetric_difference'''

set1 = {1, 2, 3, 3, 1.5}
set1.add(50)
print(set1)
value = 1
set1.add(value)  #---> if element is already present, no effect
print(set1)

s = {1, 2, True, False, 0, 3+9j}
s.add((10, 20))
print(s)

s.remove((10,20))  
print(s)
# s.remove(10)  #---> raises KeyError if the element is not present 

s.discard(10)  #---> do not raise any error
print(s)
s.discard(2)
print(s)

print(s.pop())  #---> removes an arbitrary element from the set; raises KeyError if set is empty

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1.union(s2)  #---> return a new set collection by concatenating both the sets and removing duplicates
print(s3)

s4 = s1.union({2, 3, 4}, {3, 4, 5}, {4, 5, 6}, {5, 6, 7})
print(s4)

print(s1.intersection(s2))

print(s1.difference(s2))  #---> returns a new set with elements that are not present in other set(s);
print(s2.difference(s1))  #---> returns set of elements that are only present in s2 and not in s1

print(s1.symmetric_difference(s2))  #----> returns set of all unique elements that are present in either set but not both

# Functions for Dictionary Data Items
'''
1. get
2. pop
3. popitem
4. clear
5. update
6. keys
7. values
8. items
'''

d = {1:1, 2:2, (1, 2, 3): (1, 2, 3)}
print(d.get(2))  #----> returns the value of key if present, else default

user = {
    'username' : 'user123',
    'password' : '******',
    'location' : 'IN'
}
user.pop('location')  #---> pass keyname and will delete only one key:value pair
print(user)

user = {
    'username' : 'user123',
    'password' : '******',
    'location' : 'IN'
}
user.popitem()  #---> pop key-value pairs in LIFO order
print(user)

user = {
    'username' : 'user123',
    'password' : '******',
    'location' : 'IN'
}
user.update({'password' : '123456', 'is-logged-in' : True})  #---> should be passed in the form of dictionary only
print(user)

print(user.keys())
print(user.values())
print(user.items())

# user.clear()  ---> clears the dictionary but keeps structure