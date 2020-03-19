'''class to extract courses and credit units'''

class CourseUnits:
    def __init__(self, data):
        self.__data = data

    def get(self):
        return self.__data


    # Method to return a dictionary of the courses and their credit units
    def course_and_unit(self):
        course_to_unit = list()

        for index,row in  self.get().iterrows():
            course_to_unit.append([ row['T-type'],  row['units']])
        data = dict(course_to_unit)

        return data
