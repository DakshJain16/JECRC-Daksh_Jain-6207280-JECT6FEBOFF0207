file = open('jecrc.txt', 'a+')

# file.write("JECRC is the world's best university!")
# file.write('It is popular for placements.')

file.writelines([
    '\nHere, food is good!\n',
    'ECO system is good\n',
    'Faculties are very suppotive!\n'
])
file.seek(0)
print(file.read())
file.close()