import calendar
from datetime import date
from datetime import datetime
import pickle
from Database import Stall
from Database import item
from Database import sort_data
from Database import Search_item

data_file = open("stall_info.out", mode="rb")
db = pickle.load(data_file)
data_file.close()
sort_data(db)

def check_within_opHrs(op_time, cl_time, input_time):
    if op_time==cl_time:
        return False
    else:
        op_list=op_time.split()
        cl_list=cl_time.split()
        input_list=input_time.split()

        if op_list[0]<input_list[0]<cl_list[0]:
                return True
        elif op_list[0]==input_list[0]:
            if op_list[1]<=input_list[1]:
                return True
            else:
                return False
        elif cl_list[0]==input_list[0]:
            if input_list[1]<cl_list[1]:
                return True
            else:
                return False
        else:
            return False

# Find day of the week
def findDay(year, month, day):  # month is from 1-12, day from 1-31
    dayNumber = calendar.weekday(year, month, day)
    return (dayNumber)


# Find Current Date and Time
def find_day_now():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d %m %Y")
    today = dt_string.split()
    day_of_week = findDay(int(today[2]), int(today[1]), int(today[0]))
    print (day_of_week)

def find_datetime_now():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d %m %Y")
    today=dt_string.split()

    day_of_week = findDay(int(today[2]), int(today[1]), int(today[0]))
    t_string = now.strftime("%H %M")
    print(day_of_week)
    print(t_string)

def find_time_now():
    now = datetime.now()
    # dd/mm/YY H:M:S
    t_string = now.strftime("%H %M")
    return t_string


#find_time_now()
#find_day_now()
print(check_within_opHrs("08 00", "23 00", find_time_now()))
