from cryptography.fernet import Fernet

with open('./pw.txt', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('./ende.py', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open('./ende.py', 'wb') as dec_file:
    dec_file.write(decrypted)
