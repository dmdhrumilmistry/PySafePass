# import db
import user
import logger
import functions


#-------------------- MAIN --------------------
functions.start()

username = 'Test'
website = 'testee.com'
password = 'JustTesting'
test = user.User(username, password, website)

if test.encrypt_information():
    print('[*] User data encrypted successfully')


# if test.decrypt_information():
#     print('[*] User data decrypted successfully')

print(test)