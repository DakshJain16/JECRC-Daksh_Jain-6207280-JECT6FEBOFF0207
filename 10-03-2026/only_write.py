## only_write
# file = open('temp1.txt', 'w')
# # file.write('I am the new data!')
# file.writelines([
#     'first line\n',
#     'second line\n',
#     'third line\n',
#     'fourth line\n',
#     'fifth line\n',
#     'sixth line\n'
# ])

# file.close()


## write + read
file = open('temp1.txt', 'w+')
# file.write('I am the new data!')
file.writelines([
    'first line\n',
    'second line\n',
    'third line\n',
    'fourth line\n',
    'fifth line\n',
    'sixth line\n'
])

## To make the python interpreter point at a specific index, we use seek(index)
file.seek(0)
print(file.read())

file.close()