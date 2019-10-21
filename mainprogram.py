import calendar
from datetime import date

d = date.today()
day_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
list_of_all_stall = ["McDonald", "The Sandwich Guys", "Subway", "Mini Wok", "Malay Food"]
dictionary = {'Monday' : ["Mini Wok","McDonald", "Malay Food", "Ma La Xiang Guo"],
                'Tuesday' : ["The Sandwich Guys", "McDonald", "Subway", "Cantonese"],
                'Wednesday' : ["McDonald", "Subway", "Long John"],
                'Thursday' : ["Japanese","McDonald","Chicken Rice","Malay Food"],
                'Friday' : ["Mini Wok","Subway","Long John","Starbucks"],
                'Saturday' : ["Indian","Japanese","McDonald","Mini Wok"],
                'Sunday' : ["McDonald","Subway","Long John"]}
operate_hour ={'McDonald' : "08.00-24.00",'Mini Wok' : "09.00-20.00", 'Malay Food' :"10.00-20.00",
               'Subway' : "09.00-20.00", 'The Sandwich Guys' : "08.00-19.00"}

#Display the Main Menu
def print_menu():
    choice = 0
    while choice < 1 or choice > 5:
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

#Menu when choose choice 1 (Just rough data, later can use Zi Heng's Function)
def display_menu1():
    print_stall(list_of_all_stall)
    choice1 = int(input("Enter which stall do you want :"))
    display_stall(list_of_all_stall[choice1-1])

#Find day
def findDay(day, month, year) :     
    dayNumber = calendar.weekday(year, month, day)
    thatDay = day_of_week[dayNumber]
    return thatDay

#Print Stall Based on Day
def print_stall_day(day) :
    list_stall_that_day = dictionary[day]
    for i in range(len(list_stall_that_day)) :
        print(i+1,".",list_stall_that_day[i])

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

#Check Operating Hours
def check_operating_hour(stall):
     print(operate_hour[stall])

#Calculate Queue
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
elif choice == 4 :
    stall = str(input("Enter stall : "))
    check_operating_hour(stall)
elif choice == 5 :
    stall = str(input("Enter stall : "))
    num_people = int(input("Enter number people queueing : "))
    time = check_queue(num_people)
    print("Time to wait is ",time," minutes")
