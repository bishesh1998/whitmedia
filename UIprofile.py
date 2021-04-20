from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage, QPixmap
import user
import follower
import post
import sys
from mydb import mydb
from UIpost import CreatePostUI
from UIviewpost import Viewpost
import requests
from UIuserfinder import Follow


class Profile(QtWidgets.QMainWindow):
    global mydb #global variable for the dbms access
    
    #initilizing the UI
    def __init__(self, parent = None):
        
        super(Profile, self).__init__()
        uic.loadUi('profile.ui', self)
        self.createPost = CreatePostUI(self)
        self.createPostButton.clicked.connect(self.callWritePost)
        self.viewPostUI = Viewpost(self)
        
        self.viewpostButton.clicked.connect(self.viewAllPost)
        self.searchButton.clicked.connect(self.findUser)
        #get profile information

    #fucntion query to update information of the user
    def update(self, username):
        self.username = username
        profile = user.getAccount(mydb, username)[0]
        self.user = username

        self.searchUserUI = Follow(username, self)
        self.usernameLabel.setText(profile[0])
        #self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setText(profile[1])
        self.lastNameLabel.setText(profile[2])
        self.genderValue.setText(profile[3])
        self.DoBValue.setText(str(profile[4]))
        self.followerCount.setText(str(follower.countFollowers(mydb, username)))
        self.postCount.setText(str(post.countPost(mydb,username)))

        #Pull image from Whitworth directionary
        whitworth = requests.get(f'https://www.whitworth.edu/administration/informationsystems/idcard/{self.user}.jpg')
        if whitworth.status_code == 200:
            ava  = QImage()
            ava.loadFromData(whitworth.content)
            self.ProfilePic.setPixmap(QPixmap(ava))
        self.show()

    #fucntion query to write a post    
    def callWritePost(self):
        self.createPost.updateUser(self.user)
        self.createPost.show() 

    #fucntion query to view all the post
    def viewAllPost(self):
        self.viewPostUI.update(self.username)
        self.viewPostUI.show()

    def findUser(self):
        self.searchUserUI.show()
        pass



# app = QtWidgets.QApplication(sys.argv)
# window = Profile('pcai22')
# window.show()
# app.exec()