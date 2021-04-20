from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import user
import follower
from mydb import mydb
from UIpopup import PopUp


class Follow(QtWidgets.QMainWindow):
    global mydb #global variable for the dbms access

    #initializing the UI
    def __init__(self, parent = None):
       
        super(Follow, self).__init__()
        uic.loadUi('ui/follow.ui', self)
        #self.show()
        self.followButton.clicked.connect(self.follow)
        self.successPopup = PopUp(self,"Follow successful!")
        self.failPopup = PopUp(self, "Follow fail!")
        #self.usernameLabel.setText('')

    #function to follow the user from the user input
    def follow(self):
        author = self.authorID.text()
        followerID = self.followID.text()

        if (len(user.getAccount(mydb, followerID)) == 0 or len(user.getAccount(mydb, author)) == 0):
            self.failPopup.show()
        else:
            follower.addFollowerToList(mydb, author, followerID)
            self.successPopup.show()


app = QtWidgets.QApplication(sys.argv)
window = Follow()
window.show()
app.exec()