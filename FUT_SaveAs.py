import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class SaveAsUi(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'save as: '
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getSaveFileName(self,"Save Table as: ","","All Files (*);;Text Files (*.txt)", options=options)
        if self.fileName:
            self.__repr__()

    def __repr__(self):
        return str(self.fileName)
