import time
'''
Exception Handling: 
Exception:
---> Unauthorized Event
---> Flow of execution of the program will be stopped
---> After that it will never execute the further code.
---> Syntax Error can't be handled.

Keywords used in Exception Handling:
try:
    We will put the problem statement(Block of code due to which we might get error).

except:
    We put actual solution for the error. Here solution means 'Resolution for error prone code'.
    Due to except block, we can prevent the unauthorized events(errors).
    Error colour - purple/pink ---> Exception
                 - red ---> Serious Error/issue
                 - purple ---> Warning (Code will run and display output but with warning)

finally:
    After getting error or after resolution, forcefully if we want to execute any particular
    block of code, we use finally block.

else:
    It is an alternative of try block. If we find out any error inside try block, interpreter
    will move forward towards else block. 
    If code is correct ---> output
    If code is incorrect ---> error 

Using 'raise' keyword, we can raise an exception in the program. In java, 'throws' keyword is used
for this.

Exception Handling Approaches:
---> Specific Exception Handling
---> Generic Exception Handling
---> Default Exception Handling
'''

'''
Specific Exception Handling
--> If we are aware of the error or, exception then we can go with "specific".

try:
    problem
    statement
except ErrorName:
    resolution/
    solution code
'''
# n1, n2 = 21, 0
# try:
#     result = n1 / n2
#     print(result)
# except ZeroDivisionError:
#     print('Please do no choose 0 as the second number!')

# print('Code After Try Except')

# try: 
#     a, b, c = 1, 2
# except ValueError:
#     print('For performing MVC, no of variables should be equal to no of values!')

# try:
#     print(a, b, c)
# except NameError:
#     print('Identifiers are not there in the memory!')

## keyboard interruptions
# try:
#     while True:
#         print(time.time())
# except KeyboardInterrupt:
#     print('Loop got stopped!')


'''
Generic Exception Handling
-- It is a type of exception handling approach in which there is no need to pass
any particular exception class name. Instead of we can use parent "exception" class called
'Exception'

-- Using "generic exception handling", we can't handle keyboard interruptions
'''
# try: 
#     a, b, c = 1, 2
# except Exception:
#     print('For performing MVC, no of variables should be equal to no of values!')

# try:
#     print(a, b, c)
# except Exception:
#     print('Identifiers are not there in the memory!')

## keyboard interrupt error
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('Loop got stopped!')

'''
Default Exception Handling
-- It is a type of exception handling in which we can handle all types of errors or
exceptions except "SyntaxError".
-- It cannot handle software interruptions.
'''
try:
    while True:
        print(time.time())
except:
    print('Loop got stopped!')





