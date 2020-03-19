'''Main file used that houses the sendibility of the entire model'''

import pandas as pd
import random as rd
from p_selector import Practical
from index_counter import Counter
from course_unit import CourseUnits

''' required input are the list of courses'''

class Generator:
    __DAYS = {
            1:"Monday",
            2:"Tuesday",
            3:"Wednesday",
            4:"Thursday",
            5:"Friday",
            6:"Saturday"
            }

    def __init__(self,course):
        self._course = course
        self.__df = pd.read_excel(str(self._course))
        self._semester = None # semester input by default set to none
        self._level =  None # level input by default set to none value must be an integer
        # self.__index_generator()

        ''' import parameter for the ui file and the init file'''

        self.p_day =None  # practical day
        self.unit =None # course to their credit unit
        self.info =None # Dictionary of days to required courses


    # Getter function for days
    def __days(self):
        return  Generator.__DAYS

    # getter function for data_frame
    def __get(self):
        return self.__df

    def _index_generator(self):

        df = self.__get()

        d_index = [1,2,3,4,5,6]
        d_index1 = [1,2,3,4,5]
        result =list()


        # using module p_selector to get practical day for inputed level
        p = Practical(self._semester,self._level)
        p_index = p.p_selector()
        self.p_day = self.__days()[p_index]
        d_index.remove(p_index)
        d_index1.remove(p_index)


        ''' if number of course > 8 saturday should be included '''
        ''' create a dictionary of days to courses'''

        if len(df['T-type']) <= 8:
            for index, row in df.iterrows():
                day = rd.choice(d_index1)
                equ = self.__days()[day]
                result.append([row['T-type'],equ])

        elif len(df['T-type']) > 8:
            for index,row in df.iterrows():
                day = rd.choice(d_index)
                equ = self.__days()[day]
                result.append([row['T-type'],equ])

        r_new = Counter(result)
        self.info = r_new.counter()

        ''' Create a dictionary of the course and their credit units'''

        lep = CourseUnits(self.__get())
        self.unit = lep.course_and_unit()
        return
