file = open('temp1.txt', 'r')

'''
1. read(): Display the file content as it is.
2. readline(): Display single line of data
3. readlines()
'''

print(file.read())
file.seek(0)

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)

print(file.readlines())
file.close()

# file = open('notes.txt', 'r')
# print(file.read())
# file.close()