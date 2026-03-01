'''
It is a type of statement which controls the flow of the execution of the program.
'''
## Conditional Statements: Based upon one condition, the flow of the execution of a 
## program will be decided.

'''
1. if statement (Simple if)
2. if else statement
3. elif statement
4. nested if statement
'''
## WAP to check whether the username & password is correct or not. If correct print
## login successfully completed. if not, do nothing
user = {
    'username' : 'user123',
    'password' : '*****'
}
un = input('Enter username: ')
pswd = input('Enter password: ')

# if the condition is true, then only if block will be executed.
if un == user['username'] and pswd == user['password']:
    print('Login successfully completed!')
else:
    print('Incorrect username or password!')

print('Program got ended!')

