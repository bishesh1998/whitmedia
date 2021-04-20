from PyQt5 import QtWidgets, uic
import sys
from functools import partial
from mydb import mydb

class Ui3(QtWidgets.QMainWindow):
    global mydb #global variable for the dbms access

    #initializing the UI
    def __init__(self, parent = None):
        super(Ui3, self).__init__()
        uic.loadUi('search.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.search)

    #function to get the first name of the user
    def getFirstName(self, mydb, username):
        mycursor = mydb.cursor()
        sql = "SELECT Fname, Lname FROM USER WHERE UserName = %s"
        val = (username,)

        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()

        return myresult

    #function to search the user from the first name
    def search(self):
        userName = self.textEdit.toPlainText()
        searchResult = self.getFirstName(mydb, userName)
        res = [''.join(i) for i in searchResult]
        self.listWidget.addItems(res)

app = QtWidgets.QApplication(sys.argv)
windown = Ui3()
app.exec()