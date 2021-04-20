from PyQt5 import QtWidgets, uic
import sys
from functools import partial
import user
#from UIprofile import Profile
from UIfollowprofile import FollowProfile
from mydb import mydb
from UIpopup import PopUp


class Follow(QtWidgets.QMainWindow):
    global mydb #global variable for the dbms access

    #initializing the UI
    def __init__(self, user,parent = None):

        super(Follow, self).__init__()
        uic.loadUi('userfinder.ui', self)
        self.cpopup = PopUp(self, "User Found")
        self.ipopup = PopUp(self,"User Not Found")
        self.profile = FollowProfile(user,self)

        self.seachbutton.clicked.connect(self.Search)

    #function to find the user from the input search box text     
    def Search(self):
        Searchname = self.searchbox.text()

        val = user.getAccount(mydb,Searchname)

        if (len(val) == 0):
                self.ipopup.show()
        else:
            #self.cpopup.show()
            self.profile.update(Searchname)

            

                        


if __name__ == '__main__':



    app = QtWidgets.QApplication(sys.argv)
    window = Follow("pcai22")
    window.show()
    app.exec()