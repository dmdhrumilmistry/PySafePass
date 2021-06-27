import strings
import string 
import random
import os


def print_banner():
    '''
    prints SafePass Banner
    '''
    print(strings.BANNER)


def print_menu():
    '''
    prints menu
    '''
    print(strings.MENU)


def start() -> bool:
    '''
    should run at the start of the program.
    prints banner and menu
    always returns True
    '''
    print_banner()
    print_menu()
    return True


def generate_pass(pass_len:int)->str:
    '''
    Generates random password of length which is passed as integer parameter.
    '''
    chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=/*,./;'
    random.seed = os.urandom(1024)

    for i in range(pass_len):
        passwd = ''.join(random.choice(chars) for i in range(pass_len))
        return passwd