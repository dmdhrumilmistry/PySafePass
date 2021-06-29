# SafePass

```
  ---------------------------------------------------------------------------
  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
  ---------------------------------------------------------------------------
  |                                                                         |
  |    #####     #    ####### #######    ######     #     #####   #####     |
  |   #     #   # #   #       #          #     #   # #   #     # #     #    |
  |   #        #   #  #       #          #     #  #   #  #       #          |
  |    #####  #     # #####   #####      ######  #     #  #####   #####     |
  |         # ####### #       #          #       #######       #       #    |
  |   #     # #     # #       #          #       #     # #     # #     #    |
  |    #####  #     # #       #######    #       #     #  #####   #####     |
  |                                                                         |
  ---------------------------------------------------------------------------
  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
  ---------------------------------------------------------------------------
```

SafePass is an Open Source Password Manager which stores usernames, passwords and websites with multiple user option. User can create multiple users and store their information securely from other SafePass users. Users can save and fetch passwords along with other operations using SafePass Terminal. SafePass also provides user to generate random passwords.

## About SafePass

SafePass was previously written in JAVA as random password generator, SafePass is now ported to python3 providing new features like multiple users funnctionality, options to generate, save and fetch passwords from the user stored database. 


## Dependencies


## Installation

### For Windows
- Install [Python3](https://www.python.org/) and [git](https://git-scm.com/) on your Windows.
- Check if python and git are installed and added to the path. Open Powershell or Command Prompt.
  - Python
  ```
  PS C:\Users\User> python --version
  Python 3.9.5
  ```
  - git 
  ```
  PS C:\Users\User> git --version
  git version 2.30.1.windows.1
  ```
  > Note: If your output is not similar to above, try adding python and git to environment variables path.

- Clone the SafePass repository 
  ```
  PS C:\Users\User> git clone https://github.com/dmdhrumilmistry/safepass
  ```
- Change directory to safepass
  ```
  PS C:\Users\User> cd safepass
  ```
- Install requirements
  ```
  PS C:\Users\User\safepass> pip install -r requirements.txt
  ```
- Run the safepass python file to start SafePass
  ```
  PS C:\Users\User\safepass> python safepass.py
  ```

<!-- ### For Debian based distros -->
