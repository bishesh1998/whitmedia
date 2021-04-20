from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential
from mydb import mydb
import post
import action

# User interface defined to be able to move through posts created by users followed

class Viewpost(QtWidgets.QMainWindow):
    global mydb
    def __init__(self, parent = None):
       
        super(Viewpost, self).__init__()
        uic.loadUi('ui/viewpost.ui', self)
        self.currentIndex = 0
        self.indexMax = 0
        self.nextButton.clicked.connect(self.nextPost) # moves to the next post in feed
        self.prevButton.clicked.connect(self.prevPost) # moves to the previous post in feed
        self.likeButton.clicked.connect(self.likePost) # like a post and create an action

    # update() checks the index of the post in the user's feed
    def update(self, user):
        self.currentUser = user
        postContent = post.getFollowerPosts(mydb, user, self.currentIndex)
        self.indexMax = post.countVisiblePost(mydb, user) - 1 # this is the last post in the user's feed
        self.currentPostID = postContent[0] # gets the index of the post in the feed
        self.authorLabel.setText(str(postContent[1])) 
        self.content.setText(str(postContent[2]))
        
        
        #number of likes
        likes = action.countLikes(mydb, self.currentPostID) # count the likes that a specific post has
        self.likeCount.setText(str(likes) + " likes") # outputs the number of likes in the GUI
        
        #check if the user already like the post
        if action.checkLike(mydb, self.currentUser, self.currentPostID): # checks if user already liked a post 
            self.likeButton.setText("Unlike")
            if not self.likeButton.isChecked():
                self.likeButton.toggle()
        else:
            self.likeButton.setText("Like")
            if self.likeButton.isChecked():
                self.likeButton.toggle()

    # nextPost() moves to the next posts using the index. It will be able to go from post 0 to post n and then start on post 0 again
    def nextPost(self):
        if self.currentIndex < self.indexMax:
            self.currentIndex += 1
        else:
            self.currentIndex = 0
        self.update(self.currentUser) # update based on what index the user is based on
        print(self.currentIndex)

    # prevPost() moves to the previous post using the index
    def prevPost(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
        else:
            self.currentIndex = self.indexMax
        self.update(self.currentUser)
        print(self.currentIndex)

    # likePost() creates an action if a user likes or dislikes a post. It also changes the content of the label for the GUI
    def likePost(self):
        print(self.likeButton.text())
        if self.likeButton.text() == "Like":
            action.likePost(mydb, self.currentUser, self.currentPostID) # create an action when the user likes a post
            self.likeButton.setText("Unlike")
    
        else:
            action.unlike(mydb, self.currentUser, self.currentPostID) # crate an action when the user unlikes a post
            self.likeButton.setText("Like")
        
        #number of likes
        likes = action.countLikes(mydb, self.currentPostID)
        self.likeCount.setText(str(likes) + " likes")
