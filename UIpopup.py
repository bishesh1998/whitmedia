
from PyQt5 import QtWidgets, uic, QtCore
import sys
from functools import partial
import credential


class PopUp(QtWidgets.QDialog):
    def __init__(self, parent = None, text= "Wrong username or password!"):
       
        super(PopUp, self).__init__()
        uic.loadUi('ui/wrongPassword.ui', self)
        #self.show()
        self.buttonBox.accepted.connect(self.close)
        self.label.setText(text)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.usernameLabel.setText('')