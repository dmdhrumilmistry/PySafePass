# TODO:
# 1. Create a class or functions to encrypt the database data


from cryptography.fernet import Fernet


class Encrypter:
    
    def __init__(self):
        self.KEY = Fernet.generate_key()
        self.encrypter = Fernet(self.KEY)
        # print('[*] Key Generated successfully') for logs


    def encrypt_data(self,data:str)->str:
        return self.encrypter.encrypt(data.encode()).decode()


    def decrypt_data(self, data:str)->str:
        return self.encrypter.decrypt(data.encode()).decode()


test = Encrypter()
enc = test.encrypt_data('hello')
print(enc)
dec = test.decrypt_data(enc)
print(dec)