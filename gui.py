from sys import exit, argv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLineEdit, QWidget
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
            print('{} authenticated!'.format(username))
            passwords_table = PasswordsTable()
            widget.addWidget(passwords_table)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print('Failure!! from gui')
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
            print(username)
            print(password)
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

    def get_passwords(self):
        datas = [{"username":"hello", "website":"test123", "password":"testee"},{"username":"hello123", "website":"test123123", "password":"testee123"}]
        # datas = 
        self.pass_table.setRowCount(len(datas))
        row = 0
        
        for data in datas:
            self.pass_table.setItem(row, 0, QtWidgets.QTableWidgetItem(data['username']))
            self.pass_table.setItem(row, 1, QtWidgets.QTableWidgetItem(data['website']))
            self.pass_table.setItem(row, 2, QtWidgets.QTableWidgetItem(data['password']))
            row += 1
        
        self.pass_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


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
