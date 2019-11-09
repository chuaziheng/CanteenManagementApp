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


# Find day of the week
def findDay(year, month, day):  # month is from 1-12, day from 1-31
    dayNumber = calendar.weekday(year, month, day)
    return (dayNumber)


# Find Current Date and Time
def find_datetime_now():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d %m %Y")
    today=dt_string.split()

    day_of_week = findDay(int(today[2]), int(today[1]), int(today[0]))
    t_string = now.strftime("%H %M")
    print(day_of_week)
    print(t_string)


find_datetime_now()
