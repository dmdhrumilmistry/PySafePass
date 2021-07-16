from sys import exit, argv
import random, os, string, pyperclip
import db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
from user import User


user = 'AUTH_ME'


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("UI/login.ui", self)
        self.login_button.clicked.connect(self.login_user)
        self.createacc_button.clicked.connect(self.change_to_create_acc_dialog)
        self.password_input.setEchoMode(QLineEdit.Password)

    
    def login_user(self):
        global user
        username = self.username_input.text()
        password = self.password_input.text()
        user = User(new_usr=False, usrname=username, passwd=password)
        if user.authenticate_user():
            # print('{} authenticated!'.format(username))
            passwords_table = PasswordsTable()
            widget.addWidget(passwords_table)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            # print('Failure!! from gui')
            self.username_input.setText('')
            self.password_input.setText('')

    
    def change_to_create_acc_dialog(self):
        new_acc = CreateAcc()
        widget.addWidget(new_acc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi('UI/CreateAccount.ui', self)
        self.createacc_button.clicked.connect(self.create_new_acc)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.conpassword_input.setEchoMode(QLineEdit.Password)

    
    def create_new_acc(self):
        if self.conpassword_input.text() == self.password_input.text() and len(self.username_input.text())>0:
            global user
            username = self.username_input.text()
            password = self.password_input.text()
            user = User(new_usr=True, usrname=username, passwd=password)
            # print(username)
            # print(password)
            login_page = Login()
            widget.addWidget(login_page)
            widget.setCurrentIndex(widget.currentIndex()+1)


class PasswordsTable(QDialog):
    def __init__(self):
        super(PasswordsTable, self).__init__()
        loadUi('UI/PasswordsTable.ui', self)
        self.pass_table.setColumnWidth(0,112)
        self.pass_table.setColumnWidth(1,175)
        self.pass_table.setColumnWidth(2,152)
        self.get_passwords()

        self.save_new_info_button.clicked.connect(self.save_new_info)
        self.refresh_data_button.clicked.connect(self.get_passwords)

    def save_new_info(self):
        save_info_page = SaveInformation()
        widget.addWidget(save_info_page)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def get_passwords(self):
        if user != 'AUTH_ME' and user.get_user_pass():
            data = user.data
            # print(data)

            rows_count = len(data['usernames'])
            # print(rows_count)
            self.pass_table.setRowCount(rows_count)
            
            for row in range(rows_count):
                self.pass_table.setItem(row, 0, QtWidgets.QTableWidgetItem(data['usernames'][row]))
                self.pass_table.setItem(row, 1, QtWidgets.QTableWidgetItem(data['websites'][row]))
                self.pass_table.setItem(row, 2, QtWidgets.QTableWidgetItem(data['passwords'][row]))
                row += 1
            
            self.pass_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        else:
            # print('[+] Login first or save passwords before fetching information!')
            pass


class SaveInformation(QDialog):
    def __init__(self):
        super(SaveInformation, self).__init__()
        loadUi('UI/SaveInfo.ui',self)

        self.genpass_button.clicked.connect(self.genpass)
        self.saveinfo_button.clicked.connect(self.saveinfo)


    def genpass(self):
        passwd = self.password_input.text()
        try:
            passlen = int(passwd)
        except:
            passlen = 12

        # generate random password
        chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=/*,./;'
        random.seed = os.urandom(1024)
        for i in range(passlen):
            passwd = ''.join(random.choice(chars) for i in range(passlen))
        
        pyperclip.copy(passwd)
        self.password_input.setText(passwd)


    def saveinfo(self):
        username = self.username_input.text()
        website = self.website_input.text()
        password = self.password_input.text()
        if user.add_info(username=username, password=password, website=website):
            # print('[+] Info Saved Successfully')
            message_box(box_type='info', title='Info Saved', text='Information Saved Successfully!', info_text='Press refresh button to view changes.')
            self.password_input.setText('')
            self.password_input.setText('')
            self.password_input.setText('')
        else:
            # print('[-] Error while saving info.')
            pass
        widget.setCurrentIndex(widget.currentIndex()-1)


def message_box(box_type='warning',title='Title',text='information box', info_text='more info'):
    msg = QMessageBox()
    if box_type == 'warning':
        box_type = QMessageBox.Warning
    elif box_type == 'info':
        box_type = QMessageBox.Information
    
    msg.setIcon(box_type)
    msg.setWindowTitle(title)

    msg.setText(text)
    msg.setInformativeText(info_text)
    # msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok)
    # msg.buttonClicked.connect()
	
    msg.exec_()


SafePassApp = QApplication(argv)
SafePassLoginWindow = Login()
widget = QStackedWidget()
widget.setWindowTitle('SafePass')
widget.addWidget(SafePassLoginWindow)
widget.setFixedHeight(620)
widget.setFixedWidth(480)
widget.show()


def start_safepass_app():
    global SafePassApp
    exit(SafePassApp.exec_())