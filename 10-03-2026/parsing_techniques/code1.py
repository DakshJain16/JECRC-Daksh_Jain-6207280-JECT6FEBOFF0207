import pickle
file = open('temp1.txt', 'ab+')
data = {
    'fullname' : 'Daksh Jain',
    'userid' : 3456789,
    'password' : '******'
}

# print(f'Original Data: {data}')
# print(f'Type of original data: {type(data)}')
# print()

# enc_data = pickle.dumps(data)
# print(f'Encrypted Data: {enc_data}')
# print(f'Type of Encrypted data: {type(enc_data)}')
# print()

# dec_data = pickle.loads(enc_data)
# print(f'Decrypted Data: {dec_data}')
# print(f'Type of Decrypted data: {type(dec_data)}')


enc_data = pickle.dumps(data)
file.write(enc_data)

file.seek(0)
enc_data = file.read()
print(type(enc_data))

ori_data = pickle.loads(enc_data)
print(ori_data, type(ori_data))

file.close()