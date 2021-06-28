# TODO :
# 1. Create a simple database to store username, website and password
# 2. Generate db to save keys
import sqlite3
from os.path import isfile 


def add_user(usrname:str, password_hash:str)->bool:
    '''
    adds username and its password hash to the password db.
    '''
    try:
        pass_con = sqlite3.connect('passwords.db')
        pass_cur = pass_con.cursor()
        pass_cur.execute('CREATE TABLE IF NOT EXISTS password_hashes (NAME TEXT, KEY TEXT)')
        pass_cur.execute("INSERT INTO password_hashes VALUES (?,?)",(usrname, password_hash))
        pass_con.commit()
        pass_con.close()
        print(f'[*] Successfully added password hash to db of user {usrname}')
        return True
    except Exception as e:
        print(e) 
        return False


def get_pass_hash(usrname:str)->str:
    '''
    searches for password hash in the password db for specific usrname 
    and returns passwd_hash as string
    '''
    try:
        pass_con = sqlite3.connect('passwords.db')
        pass_cur = pass_con.cursor()
        # fetch password hash for usrname from password_hashes table
        pass_cur.execute('SELECT KEY FROM password_hashes WHERE NAME=?', (usrname,))
        passwd_hash = pass_cur.fetchone()

        if passwd_hash is not None:
            # if row is not none then acc is found and fetched the password hash
            print('[*] Password hash fetched successfully from password db for user ', usrname)
            return passwd_hash[0]
        else :
            # return empty string if acc not found
            print('[!] No Account Found.')
            return ''

    except Exception as e:
        print(e) 
        return False


# Test case
# print(add_user('test', '81dc9bdb52d04dc20036dbd8313ed055'))
# print(get_pass_hash('test'))