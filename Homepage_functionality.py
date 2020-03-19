import sys
from PyQt5.QtWidgets import QTableWidgetItem
from functools import partial


class HpFunc:
    def __init__(self,view):
        self.semester = None
        self.level = None
        self.file_loc = None
        self.save_name = None
        self._hp = view
        self.info = None
        self.p_day = None
        self.data = None # dictionary of courses to their credit units
        ''' Slot of the various signals'''

        self._hp.file_toolbtn.clicked.connect(partial(self._file_locaiton))
        self._hp.s_combobox.currentTextChanged.connect(self._semester)
        self._hp.l_combobox.currentTextChanged.connect(self._level)
        self._hp.g_button.clicked.connect(partial(self._generation))
        self._hp.e_button.clicked.connect(partial(self._savepage))

    #input needed for the timetable generation are semester, level, filename, name to save as'''
    #others includes the faculty and the department

    def _file_locaiton(self):
        from FUT_FileLocation import FileLocation
        self.file_loc = str(FileLocation())
        # print(self.file_loc)
        self._hp.file_lineedit.setText(self.file_loc)


    def _savepage(self):
        from FUT_SaveAs import SaveAsUi
        self.save_name = str(SaveAsUi())

        from __init__ import createtable
        table = createtable(excelname = self.save_name, days = self.info, p_day = self.p_day, data = self.data)




    def _semester(self):
        self.semester =  self._hp.s_combobox.currentText()
        # print(self.semester)
        # print(type(self.semester))

    def _level(self):
        self.level = int(self._hp.l_combobox.currentText())
        # print(self.level)
        # print(type(self.level))

    def _generation(self):
        from timetable_generator import Generator
        table = Generator(self.file_loc)
        table._semester = self.semester
        # print(table._semester)
        table._level = self.level
        # print(table._level)

        s_table = table._index_generator()
        self.info = table.info
        self.p_day = table.p_day
        self.data = table.unit
        # print(self.info)
        self._hp.table.clearContents()

        index = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        ra = 0
        for item in index:
            day = QTableWidgetItem(item)
            self._hp.table.setItem(ra,0,day)
            ra += 1

        rol = 0
        col = 1
        for day in self.info:
            courses = self.info[day]
            for item in courses:
                course = QTableWidgetItem(item)
                self._hp.table.setItem(rol,col,course)
                col += 1
            rol += 1
            col = 1
