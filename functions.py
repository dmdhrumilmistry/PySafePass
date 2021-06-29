import strings
import string 
import random
import os
from user import User
import db
from subprocess import call 


def __print_banner():
    '''
    prints SafePass Banner
    '''
    print(strings.BANNER)


def __print_commands():
    '''
    prints menu
    '''
    print(strings.COMMANDS_LIST)


def __generate_pass(pass_len:int)->str:
    '''
    Generates random password of length which is passed as integer parameter.
    '''
    chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=/*,./;'
    random.seed = os.urandom(1024)

    for i in range(pass_len):
        passwd = ''.join(random.choice(chars) for i in range(pass_len))
        return passwd


def __save_user_pass(user:User)->bool:
    '''
    saves user password and other information to the database.
    This function is written for functions.py 
    '''
    # TODO:
    # 0. Decrypt data before saving.
    # 1. Ask for username. (done)
    # 2. Authenticate user. (optional for single user) (implemented)
    # 3. get information which is to be saved. (done)
    # 4. add and encrypt info. (done)
    # 5. save info to database. (remaining)
    user.decrypt_info()

    username = input('[+] username : ')
    password = input('[+] password : ')
    website = input('[+] website : ')

    user.add_info(username, password, website)
    user.encrypt_info()
    if db.dump_user_data(data=user.data, name=user.usrname):
        print('[*] User data has been dumped.')
    else:
        print('[!] User data has not been dumped yet! Received False')


def __get_user_pass(user:User):
    '''
    saves user password and other information to the database.
    This function is written for functions.py 
    '''
    # TODO:
    # 1. Ask for username. (done)
    # 2. Authenticate user. (optional for single user) (implemented)
    # 3. get information which is to be saved. (done)
    # 4. add and encrypt info. (done)
    # 5. save info to database. (remaining)

    data = db.get_dumped_user_data(user.usrname)
    if data:
        user.data = data
        user.decrypt_info()
    else:
        print(f'[!] Save some passwords for the user {user.usrname}')


def __show(user:User):
    '''
    prints data stored by the user.
    '''
    user.print_data()


def __clrscr():
    '''
    clears text from the screen.
    '''
    clear = 'cls' if os.name=='nt' else 'clear'
    print(clear)
    call(clear, shell=True) 


def __login()->User:
    '''
    helps user to login.
    '''
    usernames = db.get_saved_users() 
    usrname = input('[+] Enter your name : ')

    if usrname in usernames:
        return User(new_usr=False, usrname=usrname)
        

def __new_user()->User:
    '''
    Creates new user.
    '''
    usrname = input('[+] Enter your name: ')
    return User(new_usr=True,usrname=usrname)


def __get_command(user:User):
    '''
    prints menu and asks user for their choice of operation.
    '''
    choice = input('SafePass > ').lower()
    
    if choice=='newuser':
        __new_user()
    
    elif choice=='savepass':
        __save_user_pass(user)
    
    elif choice=='getpass':
        __get_user_pass(user)
    
    elif choice=='genpass':
        try :
            pass_len = int(input('[+] Enter password length : '))
            print('generated password :', __generate_pass(pass_len))
        except ValueError:
            print('[-] Enter valid length')
        except Exception as e:
            print('[-] Exception : ', e)
    
    elif choice == 'login':
        __login()

    elif choice == 'help':
        __print_commands()

    elif choice == 'clear':
        __clrscr()

    elif choice == 'exit':
        print('[*] Exiting SafePass.')
        exit()
    
    elif choice == 'show':
        __show(user)

    else :
        print('[!] INVALID COMMAND ')
        print(strings.INVALID_COMMAND)


def start() -> bool:
    '''
    should run at the start of the program.
    prints banner and menu
    always returns True
    '''
    __clrscr()
    __print_banner()
    __print_commands()

    try:
        login_not_successfull = True
        while login_not_successfull:
            login_choice = input(strings.LOGIN_PROMPT).lower()
            if login_choice == '1':
                user = __login()
                login_not_successfull = False
            elif login_choice == '2':
                user = __new_user()
                login_not_successfull = False
            else :
                print('[-] User not logged in, please try again or create new user.')

        wanna_continue = True
        while wanna_continue:
            __get_command(user)

    except KeyboardInterrupt:
        print('\n[!] Ctrl+C detected!')
        wanna_continue = False

    except Exception as e:
        print('\n[-] Exception : ', e.with_traceback())

    return True
