# TODO :
# 1. Create a simple database to store username, website and password
# 2. Generate db to save keys
import sqlite3
from os.path import isfile 

# Connect keys.db
key_con = sqlite3.connect('D:\GithubRepos\SafePass\keys.db')
# Create cursor obj
key_cur = key_con.cursor()
try:
    # create keys table
    # Note for logs 'Generating Keys database'
    key_cur.execute('CREATE TABLE keys(id integer PRIMARY KEY, name text, key text)')
except Exception as e:
    print('[*] Table keys already exits.')
finally:
    # add values to the table
    key_cur.execute("INSERT INTO keys VALUES (0,'Mangu','Psswf0')")

    # save and exit
    key_con.commit()
    key_con.close()