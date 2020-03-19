'''class to select practical day for a level which is dependant on the semester'''

class Practical:
    def __init__(self,semester,level):
        self.__semester = semester
        self.__level = level


    #Getter function for semester
    def get_semester(self):
        return str(self.__semester)


    #Getter function for level
    def get_level(self):
        return int(self.__level)


    # Conditions for the semester and level

    def p_selector(self):

        p_day = None
        s = self.get_semester()
        s = s.lower()



        if s == "first":

            if self.get_level() == 200:
                p_day = 4

            elif self.get_level() == 300:
                p_day = 1

            elif self.get_level() == 400:
                p_day = 2

            elif self.get_level() == 500:
                p_day = 3


        elif s == "second":

            if self.get_level() == 200:
                p_day = 2

            elif self.get_level() == 300:
                p_day = 4

            elif self.get_level() == 500:
                p_day = 1

        return int(p_day)
