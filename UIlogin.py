from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
from mydb import mydb
import UInewAccount
from UIpopup import PopUp
from UIprofile import Profile


class Login(QtWidgets.QMainWindow):
    global mydb #global variable for the dbms access

    #initializing the UI
    def __init__(self, parent = None):
       
        super(Login, self).__init__()
        #load the login ui file
        uic.loadUi('login.ui', self)

        #Connect function to 
        self.newAccountButton.clicked.connect(self.newAccount)
        self.LoginButton.clicked.connect(self.login)
        self.registerAccount = UInewAccount.NewAcct(self)
        self.popup = PopUp(self)
        self.profile = Profile(self)
        #self.usernameLabel.setText('')

    #function to register a new acct
    def newAccount(self):
        print("a")
        self.registerAccount.show()

    #function to check credentials from user input then login
    def login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if (credential.checkCredential(mydb, username, password)):
            print("success")
            #call the profile windows here
            self.profile.update(username)
        else:
            print("Wrong password")
            self.popup.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
