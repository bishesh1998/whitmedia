
from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
import user
from mydb import mydb
from UIpopup import PopUp

class NewAcct(QtWidgets.QMainWindow):
    global mydb #global variable for the dbms access

    #initializing the UI
    def __init__(self, parent = None, text= "Wrong username or password!"):
       
        super(NewAcct, self).__init__()
        uic.loadUi('newacct.ui', self)

        
        self.SignUpButton.clicked.connect(self.SignUp)
        self.popup = PopUp(self, "Password Does Not Match")
        self.newppop = PopUp(self,"New Account Created")

    #function query to sign up a new user account
    def SignUp(self):
        UserName = self.UserNameInput.text()
        Email = self.EmailInput.text()
        Password = self.PasswordInput.text()
        ConfirmPassword = self.ConfirmPasswordInput.text()
        FirstName = self.FirstNameInput.text()
        LastName = self.LastNameInput.text()
        Gender = self.GenderInput.text()

        temp_var = self.dateEdit.date() 
        dob = temp_var.toPyDate()
        
        #check in both the password field matches
        if (Password != ConfirmPassword):
            self.popup.show()
        else:
            self.newppop.show()
            credential.createCredential(mydb,UserName,Password,Email)
            user.createAccount(mydb,UserName,FirstName,LastName,Gender,dob)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = NewAcct()
    window.show()
    app.exec()