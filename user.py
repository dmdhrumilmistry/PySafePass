# from prettytable import PrettyTable
import encrypt
import db
from getpass import getpass
from pprint import pprint
import hash

class User:
    '''
    class User generates a user, stores data with the help of encryption.
    '''

    # TODO: 
    # 1. Dump password hash to passwords.db (passwords.db contains password hashes)
    # 2. Dump username and password to database.

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
                print('[*] Calculating password hash')
                pass_hash = hash.hashdata(self.__password)
                print('[*] Adding password hash to db')
                db.add_user(usrname=self.usrname, password_hash=pass_hash)
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


    def __get_usr_pass_hash(self)->str:
        '''
        returns stored user password hash from saved password hash database.
        '''
        # TODO: read user saved password hash from passwords.db (partially completed)
        return db.get_pass_hash(self.usrname)


    def ___authenticate_user(self)->bool:
        '''
        Autenticates user before viewing their passwords.
        '''
        for attempt in range(3):
            entered_pass = getpass(f'[+] {self.usrname} enter your password : ')
            pass_hash = hash.hashdata(entered_pass)

            usr_pass_hash = self.__get_usr_pass_hash()

            if pass_hash == usr_pass_hash:
                print(f'[*] {self.usrname} Authenticated.')
                return True                
            else :
                print(f'[!] {self.usrname} entered incorrect password, try again.')

        print(f'[!] {self.usrname}unsuccessfull attempts!')
        return False


    def __decrypt_info(self)->bool:
            '''
            decrypts all the data (information) in the user dict. 
            '''
            # check if data is encrypted
            if self.data['encrypted']:

                # TODO : Prompt user for password and if password is valid then continue.
                # 1. Prompt and take user input. (done)
                # 2. Check with saved password hashes in the password.db 
                # 3. Authenticate user (done)
                
                if self.___authenticate_user():

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
                    print(f'[!] Decrypting process interrupted due to wrong password.')

            else : 
                print('[*] Data is already decrypted.')
                return False


    def save_password(self)->bool:
        pass

    def get_password(self)->bool:
        pass
    
# Below code is for Test 
# test_usr = User()
# test_usr.add_info(username='HEllo', password='hola', website='namaste.com')
# print(test_usr.data)
# test_usr.encrypt_info()
# test_usr.decrypt_info()