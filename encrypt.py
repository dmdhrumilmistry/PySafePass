from os.path import isdir, isfile
from os import listdir
from cryptography.fernet import Fernet

def read_key()->bytes:
    with open('keys.txt', 'r+') as key_file:
        KEY = key_file.read()
        # print('KEY : ', KEY)
        key_file.close()
        return KEY.encode()
        


def generate_and_dump_key()->bool:
    try:
        key = Fernet.generate_key()
        # open key file and store generated key
        with open('keys.txt', 'w+') as key_file:
            key_file.write(key.decode())
            return True
    except Exception as e:
        print(e)
        return False
    
# key : VvK8WPJzbP1YE_huDfQeC5xrstrXhdXqRqssWqWau3A=

# Check for keys
if isfile('keys.txt'):
    print('[*] Keys found')
    
    try :
        KEY = read_key()

    except Exception as e:
        print('[-] Cannot open keys.txt')

    finally :
        try:
            encrypter = Fernet(KEY)

        except ValueError:
            print('[-] Invalid Key Found.')
            print('[*] Generating new keys...')

            if generate_and_dump_key():
                print('[*] Key generated successfully.')
                KEY = read_key()
                encrypter = Fernet(KEY)

            else:
                print('[-] Cannot Generate Keys, Exiting..')
                exit()\

        finally:
            # test = encrypter.encrypt('Hello HOLA HI HOWDY!!!!'.encode())
            # print(test)
            # print(encrypter.decrypt(test))
            pass
else :
    print('[-] Keys not found, Exiting...')
    exit()
