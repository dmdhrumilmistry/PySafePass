from prettytable import PrettyTable

class User:
    usernames = []
    passwords = []
    websites = []


    def __init__(self, username='', password='', website=''):
        if username:
            self.usernames.append(username)
            self.passwords.append(password)
            self.websites.append(website)
            print(f'Details has been saved for the {username}')

        else :
            print('User created..')
    

    def __str__(self)->PrettyTable:
        user_data = PrettyTable()
        user_data.add_column('Usernames',self.usernames)
        user_data.add_column('Passwords',self.passwords)
        user_data.add_column('Websites',self.websites)
        
        print(user_data)
        return ''