from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
from mydb import mydb
import post
import user

# User interface defined for Posts 
class CreatePostUI(QtWidgets.QDialog):
    global mydb #global variable for the dbms access

    #initilizing the UI
    def __init__(self,user, parent = None):
        super(CreatePostUI, self).__init__()
        uic.loadUi('WritePost.ui', self)
        self.POST_Button.clicked.connect(self.WritePost) # sends a signal to execute the action

    #fucntion query to update the username
    def updateUser(self, user):
        self.username = user
        
    # call the createPost() defined in the Post class. 
    def WritePost(self):
        username = self.username # user that creates the post
        content = self.InputMessage.toPlainText() # capture message from the GUI
        post.createPost(mydb, username, content)
        self.close()

