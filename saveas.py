import sys
from PyQt5.QtWidgets import QDialog,QLineEdit,QLabel,QGridLayout,QPushButton,QApplication
from functools import partial

class SaveAsUi(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Save Table")
        self.setFixedSize(350,150)
        self.layout = QGridLayout()
        self._properties()


    def _properties(self):
        label = QLabel("Save as:")
        self.edit =QLineEdit()
        self.edit.setPlaceholderText("Enter a filename e.g new.xlsx")

        ''' save and cancel buttons'''
        self.savebtn = QPushButton("Save")
        self.cancelbtn = QPushButton('Cancel')
        self.layout.addWidget(label,0,1)
        self.layout.addWidget(self.edit,0,2,1,3)
        self.layout.addWidget(self.savebtn,1,3)
        self.layout.addWidget(self.cancelbtn,1,4)
        self.setLayout(self.layout)
