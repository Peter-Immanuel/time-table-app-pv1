from timetable_generator import Generator
import xlsxwriter as w


''' function to check the credit unit of a course using data dictionary'''

def check(item,data):
    unit = None
    if data[item] == 3:
        unit = 3
    elif data[item] == 2:
        unit = 2
    else:
        unit = 1
    return unit


''' function to create an excel sheet of generated data'''

def createtable(excelname,days,p_day,data):
    index = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    headers = ['DAYS/INDEX','8-9','9-10','10-11','11-12',\
        '12-1','1-2','2-3','3-4','4-5','5-6']

     # name to save the excel file as
    workbook = w.Workbook(excelname)
    sheet = workbook.add_worksheet()

    #<--- headers---->

    sheet.write_row(0,0,headers)
    sheet.write_column(1,0,index)

    #<---- contents ---->
    rol = 1
    col = 1
    align = workbook.add_format({'align':'center'})
    for day in days:
        value = days[day]
        for item in value:
            unit = check(item,data)
            sheet.merge_range(rol,col,rol,int(col+unit - 1),item,align)
            col += unit
        rol += 1
        col = 1
    sheet.merge_range(rol,1,rol,col+9,f'Practical starts by 9.am on {p_day}',align)

    workbook.close()
