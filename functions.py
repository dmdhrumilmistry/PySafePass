import strings
import string 
import random
import os


def print_banner():
    print(strings.BANNER)


def print_menu():
    print(strings.MENU)


def start() -> bool:
    print_banner()
    print_menu()
    return True


def generate_pass(pass_len:int)->str:
    chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=/*,./;'
    random.seed = os.urandom(1024)

    for i in range(pass_len):
        passwd = ''.join(random.choice(chars) for i in range(pass_len))
        return passwd