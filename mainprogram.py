import calendar
from datetime import date
from datetime import datetime

d = date.today()
day_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
list_of_all_stall = ["McDonald", "The Sandwich Guys", "Subway", "Mini Wok", "Malay Food"]
dictionary = {'Monday' : ["Mini Wok","McDonald Breakfast","McDonald Lunch", "Malay Food", "Ma La Xiang Guo"],
                'Tuesday' : ["The Sandwich Guys", "McDonald Breakfast","McDonald Lunch", "Subway", "Cantonese"],
                'Wednesday' : ["McDonald Breakfast","McDonald Lunch", "Subway", "Long John"],
                'Thursday' : ["Japanese","McDonald Breakfast","McDonald Lunch","Chicken Rice","Malay Food"],
                'Friday' : ["Mini Wok","Subway","Long John","Starbucks"],
                'Saturday' : ["Indian","Japanese","McDonald Breakfast","McDonald Lunch","Mini Wok"],
                'Sunday' : ["McDonald Breakfast","McDonald Lunch","Subway","Long John"]}
operate_hour ={'McDonald' : "08.00-24.00",'Mini Wok' : "09.00-20.00", 'Malay Food' :"10.00-20.00",
               'Subway' : "09.00-20.00", 'The Sandwich Guys' : "08.00-19.00"}
menu_hour = {'McDonald Breakfast' : "08 00 10 59",'McDonald Lunch': "11 00 23 59",'Mini Wok' : "09 00 20 00", 
              'Malay Food' :"10 00 20 00",'Subway' : "09 00 20 00", 'The Sandwich Guys' : "08 00 19 00"}

#Find Current Date and Time
def find_datetime():
  now = datetime.now()
  # dd/mm/YY H:M:S
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  t_string = now.strftime( "%H:%M:%S")
  return print(dt_string)
  
#Display the Main Menu
def print_menu():
    choice = 0
    while choice < 1 or choice > 5:
        find_datetime()
        print("\n")
        print("Welcome to Canteen A North Spine Information System!")
        print("\n")
        print("Menu : \n1. Stall Info \n2. Current Stalls \n3. Check Stalls on Date\n4. Operating Hours\n5. Check Queue")
        choice = int(input("\nEnter your Choice : "))
    return choice

#Display Stall Information
def display_stall(name) :
    choice = 0
    while choice < 1 or choice > 4:
        print(name)
        print("\n1. Menu\n2. Operating Hours\n3. Queue\n4. Menu on Date")
        choice = int(input("\nEnter your Choice : "))

#Print All the Stall available
def print_stall(list_stall):
    for i in range(len(list_stall)):
        print(i+1,".",list_stall[i])

#Menu when choose choice 1 
def display_menu1():
    print_stall(list_of_all_stall)
    choice1 = int(input("Enter which stall do you want :"))
    display_stall(list_of_all_stall[choice1-1])

#Find day of the week
def findDay(day, month, year) :     
    dayNumber = calendar.weekday(year, month, day)
    thatDay = day_of_week[dayNumber]
    return thatDay

#Formatting opening hours into datetime format
def menu_opening_hour(stall):
    split_list = menu_hour[stall].split ()
    opening_hour = int(split_list[0])
    opening_minute = int(split_list[1])
    now = datetime.now()
    opening_hours_formatted = now.replace(hour= opening_hour, minute= opening_minute, second=0, microsecond=0)
    return opening_hours_formatted
    

#Formatting closing hours into datetime format
def menu_closing_hour(stall):
    split_list = menu_hour[stall].split ()
    closing_hour = int(split_list[2])
    closing_minute = int(split_list[3])
    now = datetime.datetime.now()
    opening_hours_formatted = now.replace(hour= opening_hour, minute= opening_minute, second=0, microsecond=0)
    return closing_hours_formatted

#Print Stall Based on Day (Function C)
def print_stall_day(day) :
    # need to include time as well 
    list_stall_that_day = dictionary[day]
    for i in range(len(list_stall_that_day)) :
        print(i+1,".",list_stall_that_day[i])
#print stall based on time (Function C) (halfway done)
    for stall,timing in menu_hour:
        while menu_opening_hour() < now < menu_closing_hour() :
           print(stall)
def print_stall_again(day):
    if day == "Monday" :
        print_stall_day("Monday")
    elif day == "Tuesday" :
        print_stall_day("Tuesday")
    elif day == "Wednesday" :
        print_stall_day("Wednesday")
    elif day == "Thursday" :
        print_stall_day("Thursday")
    elif day == "Friday" :
        print_stall_day("Friday")
    elif day == "Saturday" :
        print_stall_day("Saturday")
    else :
        print_stall_day("Sunday")

#Check Operating Hours (Feature F)
def check_operating_hour(stall):
     print(operate_hour[stall])

#Calculate Queue (Feature E)
def check_queue(people):
    time = float(people * 2.5)
    return time

#Main Program
choice = print_menu()

if choice == 1 :
    display_menu1()
elif choice == 2 :
    year = d.year
    month = d.month
    day = d.day
    thisDay = findDay(day, month, year)
    print_stall_again(thisDay)
elif choice == 3 :
    day, month, year = input("Enter date (DD MM YYYY) : ").split()
    day = int(day)
    month = int(month)
    year = int(year)
    thatDay = findDay(day, month, year)
    print_stall_again(thatDay)
    #need to include time 

elif choice == 4 :
    stall = str(input("Enter stall : "))
    check_operating_hour(stall)
elif choice == 5 :
    stall = str(input("Enter stall : "))
    num_people = int(input("Enter number people queueing : "))
    time = check_queue(num_people)
    print("Time to wait is ",time," minutes")
