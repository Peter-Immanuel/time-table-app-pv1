''' class to count the numbers of courses in a day and returns a dict of the days and a list of their courses'''

class Counter:
    def __init__(self,result):
        self.__result = result

    # Getter function
    def get(self):
        return self.__result

    # Method to count the courses in a day and return a dict of the days and a list of their courses
    def counter(self):
        m_count = t_count = w_count = th_count = f_count = s_count = 0

        d_list = dict(monday = list(),
                      tuesday = list(),
                      wednesday = list(),
                      thursday = list(),
                      friday = list(),
                      saturday = list()
                      )

        for lst in self.get():
             for item in lst:
                if 'Monday' in item:
                     d_list['monday'].append(lst[0])

                elif 'Tuesday' in item:
                    d_list['tuesday'].append(lst[0])

                elif 'Wednesday' in item:
                    d_list['wednesday'].append(lst[0])

                elif 'Thursday' in item:
                    d_list['thursday'].append(lst[0])

                elif 'Friday' in item:
                    d_list['friday'].append(lst[0])

                elif 'Saturday' in item:
                    d_list['saturday'].append(lst[0])

        return d_list
