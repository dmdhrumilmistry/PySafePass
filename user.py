import encrypt
import db
from getpass import getpass
import hash
from prettytable import PrettyTable


class User:
    '''
    class User generates a user, stores data with the help of encryption.
    '''


    def __init__(self, new_usr:bool, usrname:str)->None:
        '''
        create User
        takes new_user (bool) as parameter 
        '''
        # create dictionary with lists to store information
        self.data = {
                'usernames': [],
                'passwords': [],
                'websites': [],
                'encrypted' : False 
        }

        usr_flag = False
        if type(usrname) is str and usrname!='' :
            self.usrname = usrname
            usr_flag = True

        if new_usr:
            print('[*] Generating new user...')

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

            else:
                print('[-] Cannot create user. Please try again.')

        else :
            # retrieving user password since user exists
            auth_result = self.___authenticate_user()
            if auth_result[0]:
                self.__password = auth_result[1]


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
            KEY = encrypt.gen_key_from_pass(self.__password) # this is where error occurred
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
            return True

        else : 
            print('[*] Data is already encrypted.')
            return False


    def __get_usr_pass_hash(self)->str:
        '''
        returns stored user password hash from saved password hash database.
        '''
        return db.get_pass_hash(self.usrname)


    def ___authenticate_user(self)->tuple():
        '''
        Autenticates user before viewing their passwords.
        returns (result, password)
        '''
        passwd = ''
        for attempt in range(3):
            entered_pass = getpass(f'[+] {self.usrname} enter your password : ')
            pass_hash = hash.hashdata(entered_pass)

            usr_pass_hash = self.__get_usr_pass_hash()

            if pass_hash == usr_pass_hash and usr_pass_hash != '':
                passwd = entered_pass
                print(f'[*] {self.usrname} Authenticated.')
                return (True, passwd)            
            else :
                print(f'[!] {self.usrname} entered incorrect password, try again.')

        print(f'[!] {self.usrname} unsuccessfull attempts!')
        return (False, passwd)


    def decrypt_info(self)->bool:
            '''
            decrypts all the data (information) in the user dict. 
            '''
            # check if data is encrypted
            if self.data['encrypted']:
                
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
                return True

            else : 
                print('[*] Data is already decrypted.')
                return False


    def print_data(self)->None:
        print(f'[!] Printing data for {self.usrname}.')

        if not self.data['encrypted']:
            # print table if data is not encrypted 
            table = PrettyTable()
            max_count = len(self.data['usernames'])
            table.add_column('SR. NO.', [ count+1 for count in range(max_count)] )
            table.add_column('USERNAMES', self.data['usernames'])
            table.add_column('WEBSITES', self.data['websites'])
            table.add_column('PASSWORDS', self.data['passwords'])
            print(table)

        else :
            print('[!] Data is encrypted.')
