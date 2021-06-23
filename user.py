from prettytable import PrettyTable
from encrypt import Encrypter


class User:
    usernames = []
    passwords = []
    websites = []


    def __init__(self, username='', password='', website=''):
        if username:
            self.usernames.append(username)
            self.passwords.append(password)
            self.websites.append(website)

            print(f'Details has been saved for {username}')

        else :
            print('User created..')
    

    def __str__(self)->str:
        '''
        prints user saved information.
        '''
        user_data = PrettyTable()
        user_data.add_column('Usernames',self.usernames)
        user_data.add_column('Passwords',self.passwords)
        user_data.add_column('Websites',self.websites)
        
        print(user_data)
        return ''

    
    def encrypt_information(self):
        '''
        Encrypts all the information provided by the user in usernames, websites and passwords list.
        '''
        pass


    def decrypt_information(self):
        '''
        Decrypts all the information available in the usernames, websites and passwords list.
        '''
        pass