from prettytable import PrettyTable
from encrypt import Encrypter


class User:
    usernames = []
    passwords = []
    websites = []

    enc_usernames = []
    enc_websites = []
    enc_passwords = []


    def __init__(self, username='', password='', website=''):
        if username:
            self.usernames.append(username)
            self.passwords.append(password)
            self.websites.append(website)
            self.encrypter = Encrypter()

            print(f'Details has been saved for {username}')

        else :
            print('User created..')
    

    def __str__(self)->str:
        '''
        prints user saved information.
        '''

        print('\n[+] Initial Data')
        user_data = PrettyTable()
        user_data.add_column('Usernames', self.usernames)
        user_data.add_column('Passwords', self.passwords)
        user_data.add_column('Websites', self.websites)
        
        print(user_data)

        # print('\n[+] Encrypted Data')
        # user_data = PrettyTable()
        # user_data.add_column('Usernames', self.enc_usernames)
        # user_data.add_column('Passwords', self.enc_passwords)
        # user_data.add_column('Websites', self.enc_websites)
        
        # print(user_data)

        # print('\n[+] Decrypted Data')
        # user_data = PrettyTable()
        # user_data.add_column('Usernames', self.usernames)
        # user_data.add_column('Passwords', self.passwords)
        # user_data.add_column('Websites', self.websites)
        
        # print(user_data)
        return ''


    
    def perform_on_list(self, func, lst):
        '''
        performs the function passed on the list.
        '''
        new_list = []
        for element in lst:
            new_list.append(func(element))

        return new_list


    def encrypt_information(self)-> bool:
        '''
        Encrypts all the information provided by the user in usernames, websites and passwords list.
        '''
        try:
            self.enc_usernames = self.perform_on_list(self.encrypter.encrypt_data, self.usernames)
            self.enc_websites = self.perform_on_list(self.encrypter.encrypt_data, self.websites)
            self.enc_passwords = self.perform_on_list(self.encrypter.encrypt_data, self.passwords)
            return True
        except Exception as e:
            print('[-] An exception occured while encrypting user data')
            print(e)
            return False        


    def decrypt_information(self):
        '''
        Decrypts all the information available in the usernames, websites and passwords list.
        '''
        try:
            self.usernames = self.perform_on_list(self.encrypter.decrypt_data, self.usernames)
            self.websites = self.perform_on_list(self.encrypter.decrypt_data , self.websites)
            self.passwords = self.perform_on_list(self.encrypter.decrypt_data, self.passwords)
            return True
        except Exception as e:
            print('[-] An exception occured while encrypting user data')
            print(e)
            return False 