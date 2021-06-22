import strings


def print_banner():
    print(strings.BANNER)


def print_menu():
    print(strings.MENU)


def start() -> bool:
    print_banner()
    print_menu()
    return True