from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage, QPixmap
import user
import follower
import sys
from mydb import mydb
from UIpost import CreatePostUI
from UIviewpost import Viewpost
import requests
from UIpopup import PopUp


class FollowProfile(QtWidgets.QMainWindow):
    global mydb 
    def __init__(self, authorID, parent = None):
        
        super(FollowProfile, self).__init__()
        uic.loadUi('followprofile.ui', self)
        self.authorID = authorID
        #connect the follow button to follow function
        self.followbutton.clicked.connect(self.follow)
        self.cpopup = PopUp(self, "User is followed !")
        #get profile information

    #update the windows to reflect the current user
    def update(self, username):
        self.username = username
        profile = user.getAccount(mydb, username)[0]
        self.user = username
        self.usernameLabel.setText(profile[0])
        #self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setText(profile[1])
        self.lastNameLabel.setText(profile[2])
        self.genderValue.setText(profile[3])
        self.DoBValue.setText(str(profile[4]))
        self.followerCount.setText(str(follower.countFollowers(mydb, username)))

        #try to pull image from Whitworth
        whitworth = requests.get(f'https://www.whitworth.edu/administration/informationsystems/idcard/{self.user}.jpg')
        if whitworth.status_code == 200:
            ava  = QImage()
            ava.loadFromData(whitworth.content)
            self.ProfilePic.setPixmap(QPixmap(ava))
        self.show()

    def follow(self):
        follower.addFollowerToList(mydb,self.authorID,self.user)
        self.cpopup.show() 



