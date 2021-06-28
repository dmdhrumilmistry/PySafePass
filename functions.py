import strings
import string 
import random
import os
from user import User
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


def __save_user_pass()->bool:
    pass


def __get_user_pass():
    pass


def __clrscr():
    '''
    clears text from the screen.
    '''
    clear = 'cls' if os.name=='nt' else 'clear'
    print(clear)
    call(clear, shell=True) 


def __get_choice():
    '''
    prints menu and asks user for their choice of operation.
    '''
    choice = input('SafePass > ')

    if choice=='1':
        user = User()
    
    elif choice=='2':
        __save_user_pass()
    
    elif choice=='3':
        __get_user_pass()
    
    elif choice=='4':
        try :
            pass_len = int(input('[+] Enter password length : '))
            print('generated password :', __generate_pass(pass_len))
        except ValueError:
            print('[-] Enter valid length')
        except Exception as e:
            print('[-] Exception : ', e)
    
    elif choice.lower() == 'help':
        __print_commands()

    elif choice.lower() == 'clear':
        __clrscr()

    elif choice.lower() == 'exit':
        print('[*] Exiting SafePass.')
        exit()

    else :
        print('[!] INVALID OPERATION ')
        print(strings.INVALID_CHOICE)


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
        wanna_continue = True
        while wanna_continue:
            __get_choice()

    except KeyboardInterrupt:
        print('\n[!] Ctrl+C detected!')
        wanna_continue = False

    except Exception as e:
        print('\n[-] Exception : ', e)

    return True
