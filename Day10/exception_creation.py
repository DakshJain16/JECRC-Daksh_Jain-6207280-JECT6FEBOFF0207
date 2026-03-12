'''
raise --> It is a keyword, which helps us to throw an error in between a program.
Exception Creation:
1. Custom Exception --> raise
2. User-defined Exception --> raise
3. Assertion Exception --> assert
'''

'''
Custom Exception:
    1. We use pre-buit Exception classes according to our requirement.

    raise ValueError('message')

    ValueError: message
'''

# num = 19
# if num >= 18:
#     print('You are eligible for voting & driving')
# else:
#     raise ValueError('Age should be greater than or equals to 18!')

'''
User-defined Exception
    1. It is a type of exception in which we can create our own exception classes
    based upon our own requirement. We can also provide names to those classes according
    to the use cases.
'''
# class MyException(Exception):
#     pass

# raise MyException('This is my Exception Class!')

# n1, n2 = 10, 0
# if n2 == 0:
#     raise MyException('Second num cannot be zero!')
# else:
#     print(n1 / n2)

'''
Assertion Exception

-- Assertion Exception can be created by using one keyword called "assert".

assert <condition>, print(ERROR)
print(output)
'''
s = input('Enter a string: ')
assert s == s[::-1], print('It is not a palindromic string!')
print('It is a palindromic string!')