# TODO:
# 1. Create a class or functions to encrypt the database data

# test

from cryptography.fernet import Fernet


KEY = Fernet.generate_key()
encrypter = Fernet(KEY)


def encrypt_data(data:str)->str:
    return encrypter.encrypt(data.encode()).decode()


def decrypt_data(data:str)->str:
    return encrypter.decrypt(data.encode()).decode()


# TEST
# mess = 'HEllo'
# enc_mess = encrypt_data(mess)
# print(enc_mess)
# print(decrypt_data(enc_mess))