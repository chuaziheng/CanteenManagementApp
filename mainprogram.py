from datetime import date
import calendar

today = date.today()
list_of_all_stall = ["McDonald", "The Sandwich Guys", "Subway", "Mini Wok", "Malay Food"]
list_of_stall_monday = ["McDonald","Mini Wok","Japanese Food"]

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
def print_stall():
    for i in range(len(list_of_all_stall)):
        print(i+1, list_of_all_stall[i])

#Menu when choose choice 1 (Just rough data, later can use Zi Heng's Function)
def display_menu1():
    print_stall()
    choice1 = int(input("Enter which stall do you want :"))
    display_stall(list_of_all_stall[choice1-1])

#Find day
def findDay(date) :
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    return dayNumber 

#Main Program
choice = print_menu()

if choice == 1 :
    display_menu1()
elif choice == 2 :
    date_today = today.strftime("%d %m %Y")
    day = findDay(date_today)
    if day == 0:
        
        
                    
    

  


