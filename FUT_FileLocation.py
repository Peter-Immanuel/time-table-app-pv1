import sys
from PyQt5.QtWidgets import QDialog,QApplication,QWidget, QInputDialog,QFileDialog,QLineEdit

class FileLocation(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'My safe from dialog'
        self.top = 10
        self.left = 10
        self.width = 640
        self.height = 480
        filename = self.initUi()


    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select file", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            self.__repr__()

    def __repr__(self):
        return str(self.fileName)
