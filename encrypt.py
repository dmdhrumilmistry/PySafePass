# TODO:
# 1. Create a class or functions to encrypt the database data

from cryptography.fernet import Fernet


class Encrypter:
    
    def __init__(self):
        # generate and store key
        KEY = Fernet.generate_key()
        with open('keys.txt', 'r+') as key_file:
            key_file.write(KEY.decode())

        self.encrypter = Fernet(KEY)
        # print('[*] Key Generated successfully') #for logs


    def encrypt_data(self,data:str)->str:
        '''
        Encrypts data with help of secret key
        '''
        return self.encrypter.encrypt(data.encode()).decode()


    def decrypt_data(self, data:str)->str:
        '''
        Decrypts data with help of secret key
        '''
        return self.encrypter.decrypt(data.encode()).decode()


    def __get_key(self)->bytes:
        with open('keys.txt', 'r') as key_file:
            key = key_file.read()
            return key.encode()


test = Encrypter()

enc = test.encrypt_data('hello')
print(enc)

dec = test.decrypt_data(enc)
print(dec)