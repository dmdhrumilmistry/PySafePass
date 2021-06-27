# from prettytable import PrettyTable
import encrypt
from getpass import getpass

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
            passwd1 = getpass('[+] Choose your password :')
            passwd2 = getpass('[+] Verify your password : ')

            if passwd1 == passwd2:
                pass_flag = True
                self.__password = passwd1
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
                    'websites': []
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
            

    def encrypt_info(self):
        '''
        encrypts all the data (information) in the user list. 
        '''
        KEY = encrypt.gen_key_from_pass(self.__password)

        # TODO : Encrypt data from list using encrypt.encrypt_data(KEY, data) and store it into another list 
        # usernames =  [ self.fernet.decrypt(self.usernames[pos].encode()).decode() for pos in range(len(data['usernames'])) ]
         
        

test_usr = User()
test_usr.add_info(username='HEllo', password='hola', website='namaste.com')
print(test_usr.data)