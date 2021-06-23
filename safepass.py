import db
import user
import logger
import functions


#-------------------- MAIN --------------------
functions.start()

username = 'Test'
website = 'testee.com'
password = 'JustTesting'
test = user.User(username, password, website)



print(test)