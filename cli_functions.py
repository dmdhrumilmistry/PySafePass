import strings
import string 
import random
import os
import logger
from user import User
import db
from subprocess import call 
from pyperclip import copy


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
        logger.info('[*] Copying generated password to clipboard.')
        copy(passwd)
        return passwd


def __save_user_pass(user:User)->bool:
    '''
    saves user password and other information to the database.
    This function is written for functions.py 
    '''
    user.decrypt_info()

    username = input('[+] username : ')
    password = input('[+] password : ')
    website = input('[+] website : ')

    user.add_info(username, password, website)
    user.encrypt_info()
    if db.dump_user_data(data=user.data, name=user.usrname):
        logger.info('[*] User data has been dumped.')
    else:
        logger.warning('[!] User data has not been dumped yet! Received False')


def __get_user_pass(user:User):
    '''
    saves user password and other information to the database.
    This function is written for functions.py 
    '''
    data = db.get_dumped_user_data(user.usrname)
    if data:
        user.data = data
        user.decrypt_info()
    else:
        logger.warning('[!] Save some passwords for the user {user.usrname}')


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
            logger.error('[-] Enter valid length')
        except Exception as e:
            logger.error('[-] Exception : ', e)
    
    elif choice == 'login':
        __login()

    elif choice == 'help':
        __print_commands()

    elif choice == 'clear':
        __clrscr()

    elif choice == 'exit':
        logger.info('[*] Exiting SafePass.')
        exit()
    
    elif choice == 'show':
        __show(user)

    else :
        logger.warning('[!] INVALID COMMAND ')
        print(strings.INVALID_COMMAND)


def start_console() -> bool:
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
                logger.info('[-] User not logged in')
                print('[-] User not logged in, please try again or create new user.')


        wanna_continue = True
        while wanna_continue:
            __get_command(user)

    except KeyboardInterrupt:
        logger.warning('\n[!] Ctrl+C detected!')
        print('\n[!] Ctrl+C detected!')
        wanna_continue = False

    except Exception as e:
        logger.info('\n[-] Exception : ' + str(e))

    return True
