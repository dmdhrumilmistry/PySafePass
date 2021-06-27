# from prettytable import PrettyTable
from inspect import indentsize
from sqlite3.dbapi2 import SQLITE_DELETE
import encrypt
from getpass import getpass
from pprint import pprint


class User:
    def __init__(self)->None:
        print('[*] Generating new user...')

        usr_flag = False
        usrname = input('[+] Enter your name: ')
        if type(usrname) is str and usrname!='' :
            self.usrname = usrname
            usr_flag = True
        
        pass_flag = False
        for attempt in range(3):
            __passwd1 = getpass('[+] Choose your password :')
            __passwd2 = getpass('[+] Verify your password : ')

            if __passwd1 == __passwd2:
                pass_flag = True
                self.__password = __passwd1
                print('[*] Password Matched.')
                break
            else: 
                print('[-] Passwords do not match. Please try again.')                

        if usr_flag and pass_flag :
            print('[*] User created with username {}'.format(self.usrname))

            # create dictionary with lists to store information
            self.data = {
                    'usernames': [],
                    'passwords': [],
                    'websites': [],
                    'encrypted' : False 
            }

        else:
            print('[-] Cannot create user. Please try again.')


    # TODO: 
    # 1. Dump password hash to passwords.db (passwords.db contains password hashes)
    # 2. Dump username and password to database.


    def add_info(self, username, password, website)->bool:
        '''
        add user entered information to the lists.
        returns bool.
        '''
        print('[*] Adding Information to the lists')
        # if any parameter is empty, print error
        if bool(username) and bool(password) and bool(website):
            self.data['usernames'].append(username)
            self.data['passwords'].append(password)
            self.data['websites'].append(website)
            print('[*] Information added to list successfully.')
            return True
        else:
            print('[-] Please enter valid information. All parameters should be non empty.')
            return False
            

    def encrypt_info(self)->bool:
        '''
        encrypts all the data (information) in the user dict. 
        '''
        # check if data is not encrypted
        if not self.data['encrypted']:
            KEY = encrypt.gen_key_from_pass(self.__password)
            length = len(self.data['usernames'])

            # encrypt data into a new list
            usernames = [ encrypt.encrypt_data( KEY, self.data['usernames'][pos] ).decode('utf-8') for pos in range(length) ]
            passwords = [ encrypt.encrypt_data( KEY, self.data['passwords'][pos] ).decode('utf-8') for pos in range(length) ]
            websites = [ encrypt.encrypt_data( KEY, self.data['websites'][pos] ).decode('utf-8') for pos in range(length) ]
            
            # update data values
            self.data['usernames'] = usernames
            self.data['passwords'] = passwords
            self.data['websites'] = websites
            self.data['encrypted'] = True

            print('[*] Encrypted Data successfully')
            pprint(self.data)
            return True

        else : 
            print('[*] Data is already encrypted.')
            return False


    def decrypt_info(self)->bool:
            '''
            decrypts all the data (information) in the user dict. 
            '''
            # check if data is encrypted
            if self.data['encrypted']:

                # TODO : Prompt user for password and if password is valid then continue.
                # 1. Prompt and take user input.
                # 2. Check with saved password hashes in the password.db 
                # 3. Authenticate user
                
                KEY = encrypt.gen_key_from_pass(self.__password)
                length = len(self.data['usernames'])

                # decrypt data into a new list
                usernames = [ encrypt.decrypt_data( KEY, self.data['usernames'][pos] ).decode('utf-8') for pos in range(length) ]
                passwords = [ encrypt.decrypt_data( KEY, self.data['passwords'][pos] ).decode('utf-8') for pos in range(length) ]
                websites = [ encrypt.decrypt_data( KEY, self.data['websites'][pos] ).decode('utf-8') for pos in range(length) ]
                
                # update data values
                self.data['usernames'] = usernames
                self.data['passwords'] = passwords
                self.data['websites'] = websites
                self.data['encrypted'] = False

                print('[*] Decrypted Data successfully')
                pprint(self.data)
                return True

            else : 
                print('[*] Data is already decrypted.')
                return False

# Below code is for Test 
test_usr = User()
test_usr.add_info(username='HEllo', password='hola', website='namaste.com')
print(test_usr.data)
test_usr.encrypt_info()
test_usr.decrypt_info()