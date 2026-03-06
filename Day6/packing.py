'''
Single or Tuple Packing
def func_name(*args):
    Statement
    Block
func_name(val1, val2, val3, ...., valn)
'''

## create a function which can take n no of int or float numbers and returns only their addition

# def add_num(*args):
#     print(args,  type(args))
#     sum = 0
#     for i in args:
#         sum += i
#     print(f'Addition : {sum}')

# add_num()
# add_num(1, 2, 3, 4, 5, 1.9, 98.2, 1)

# def add_num(*args):
#     args = list(args)
#     print(args,  type(args))
#     sum = 0
#     for i in args:
#         sum += i
#     print(f'Addition : {sum}')

# add_num()
# add_num(1, 2, 3, 4, 5)

'''
create a function which will take n no of inputs from the user and return the sum of only int & floating point numbers. 
Please make sure that, user is capable of passing all type of values
'''

# def add_num(*args):
#     print(args, type(args))
#     sum = 0
#     for i in args:
#         if type(i) in [float, int]:
#             sum += i
#     print(f'Addition : {sum}')

# add_num(1, 2, 1.1, 3+9j, 'abc', False, 'hello', [1, 2, 3])

# l1 = []
# while True:
#     user_input = eval(input())
#     if user_input == "Null":
#         break
#     else:
#         l1.append(user_input)

# add_num(*l1)

# add_num(*eval(input('Enter a list of values: ')))  #---> unpacking; we put * to unpack 

'''
Double or Dictionary Packing
def func_name(**kwargs):
    Statement
    Block
    
func_name(k1=v1, k2=v2, ....., kn=vn)
All the key names should be a string but you can't use quotes.
'''

# def print_details(**kwargs):
#     print(kwargs)

# print_details(username = 'user123', password = '****', logged_in_devices = ['Android', 'Windows', 'Linux'])

'''create a function which will return a list of prime numbers. Please make sure that user can pass n no. of inputs.
For checking whether a number is prime or not, you can create one function
'''

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True
 
def find_prime_num(*args):
    prime = []
    for i in args:
        if is_prime(i):
            prime.append(i)
    
    return prime

print(find_prime_num(*eval(input('Enter a list of nums: '))))