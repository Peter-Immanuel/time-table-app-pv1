''' python source code for the GUI of the project in python3'''

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFrame,QGridLayout,QHBoxLayout,QWidget
from PyQt5.QtWidgets import QLabel,QComboBox,QPushButton,QSpacerItem,QSizePolicy,QTableWidget
from PyQt5.QtWidgets import QLineEdit,QAbstractItemView,QTableWidgetItem
from PyQt5 import QtCore
from Homepage_functionality import HpFunc


class FutUi(QMainWindow):
    def __init__(self):

        '''initializing the ui'''

        super().__init__()
        self.setWindowTitle("FUTMINNA APP")
        self.resize(651, 584)
        self.generallayout = QGridLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generallayout)
        self._createdisplay()


    def _createdisplay(self):

        spacer = QSpacerItem(40, 20,QSizePolicy.Expanding,QSizePolicy.Minimum)

        ''' File location '''
        # file label, lineEdit and tool button

        file_label = QLabel("File:")
        file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_lineedit = QLineEdit()
        self.file_lineedit.setPlaceholderText("---select file location---")
        self.file_lineedit.setReadOnly(True)
        self.file_toolbtn = QPushButton('...')
        self.file_toolbtn.setFixedSize(26,22)

        layout = QGridLayout()
        layout.addWidget(file_label,0,0)
        layout.addWidget(self.file_lineedit,0,1,1,4)
        layout.addWidget(self.file_toolbtn,0,5)

        ''' semester and level selector'''

        # semester label and combobox
        s_label = QLabel("Semester:")
        s_label.setAlignment(QtCore.Qt.AlignCenter)
        self.s_combobox = QComboBox()
        self.s_combobox.addItem("--select--")
        self.s_combobox.addItem('First')
        self.s_combobox.addItem('Second')

        # semester and label layouts
        s_layout = QHBoxLayout()
        s_layout.addWidget(s_label)
        s_layout.addWidget(self.s_combobox)

        # level label and combo box
        l_label = QLabel("Level:")
        l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_combobox = QComboBox()
        self.l_combobox.addItem('--select--')
        #self.l_combobox.addItem('100')
        self.l_combobox.addItem('200')
        self.l_combobox.addItem('300')
        self.l_combobox.addItem('400')
        self.l_combobox.addItem('500')

        #level layout
        l_layout = QHBoxLayout()
        l_layout.addWidget(l_label)
        l_layout.addWidget(self.l_combobox)

        # semester and level layout. ALso the layout for the file lineEdit id included
        S_L_layout = QGridLayout()
        S_L_layout.addLayout(layout,0,0,1,4)
        S_L_layout.addLayout(s_layout,1,0)
        S_L_layout.addLayout(l_layout,2,0)

        # semester and level frame
        s_frame = QFrame()
        s_frame.setLayout(S_L_layout)
        s_frame.setFrameShadow(QFrame.Raised)
        s_frame.setFrameShape(QFrame.StyledPanel)

        self.generallayout.addWidget(s_frame,0,0)
        #self.generallayout.addItem(spacer,1,1,1,2)



        ''' Faculty and Department selector'''

        # faculty selector
        f_label = QLabel("Faculty:")
        f_label.setAlignment(QtCore.Qt.AlignCenter)
        f_combo = QComboBox()
        f_combo.addItem('--select--')
        f_combo.addItem("SEET")
        f_combo.addItem("SAAT")
        f_combo.addItem("SET")
        f_combo.addItem("SICT")
        f_combo.addItem("SEMT")


        # faculty layout
        f_layout = QHBoxLayout()
        f_layout.addWidget(f_label)
        f_layout.addWidget(f_combo)


        # Department selector
        d_label = QLabel("Department:")
        d_label.setAlignment(QtCore.Qt.AlignCenter)
        d_combo = QComboBox()
        d_combo.addItem('--select--')
        d_combo.addItem('ABE')
        d_combo.addItem('CIVIL')
        d_combo.addItem('COMPUTER')
        d_combo.addItem('TELECOMS')
        d_combo.addItem('MAT & MET')
        d_combo.addItem('CHEMICAL')
        d_combo.addItem('MECHANICAL')
        d_combo.addItem('MECHATRONICS')

        # department layout
        d_layout = QHBoxLayout()
        d_layout.addWidget(d_label)
        d_layout.addWidget(d_combo)


        # faculty and department layout
        f_d_layout = QGridLayout()
        f_d_layout.addLayout(f_layout,1,3)
        f_d_layout.addLayout(d_layout,2,3)

        # faculty and department frame

        f_d_frame = QFrame()
        f_d_frame.setLayout(f_d_layout)
        f_d_frame.setFrameShadow(QFrame.Raised)
        f_d_frame.setFrameShape(QFrame.StyledPanel)
        self.generallayout.addWidget(f_d_frame,0,4)

        ''' table view widget '''
        index = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


        self.table = QTableWidget(7,8)
        rol = 0
        for item in index:
            day = QTableWidgetItem(item)
            self.table.setItem(rol,0,day)
            rol += 1

        self.table.setShowGrid(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # table layout
        table_layout = QGridLayout()
        table_layout.addWidget(self.table,0,0,1,5)

        # table view frame
        t_frame = QFrame()
        t_frame.setLayout(table_layout)
        t_frame.setFrameShadow(QFrame.Raised)
        t_frame.setFrameShape(QFrame.StyledPanel)
        self.generallayout.addWidget(t_frame,1,0,3,5)



        ''' push pushbuttons '''

        self.g_button = QPushButton("Generate")
        self.e_button = QPushButton("Export")

        # buttons layout
        btn_layout = QGridLayout()
        btn_layout.addWidget(self.g_button,5,0)
        btn_layout.addWidget(self.e_button,5,1)

        # button frame
        btn_frame = QFrame()
        btn_frame.setLayout(btn_layout)
        self.generallayout.addWidget(btn_frame,5,2)



if __name__ == "__main__":
    fut = QApplication(sys.argv)
    app = FutUi()
    app.show()
    HpFunc(view = app)
    sys.exit(fut.exec_())
