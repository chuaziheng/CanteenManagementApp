#entire file done by Bodipati Kiran
#this file mainly deals with the definition of data structures, and creation and storage of database

import pickle
#for loading data into binary file


#A class defined to handle the data structure item of a menu, with attributes being item_name and price
class item:
    def __init__(self, item_name="", price=0.0): # constructor to initialize the object.
        self.item_name = item_name
        self.price = price


def input_item():  # to input the item
    item_name = input("Enter item name")
    item_price = float(input("enter item price"))
    return item(item_name, item_price)


class Stall: #class definition to store the information of a stall.
    def __init__(self, st_name="", desc="", prep_time=0.0, halal=False, menu1=[], menu2=[], opening_time=[],
                 closing_time=[], changeover_time=[]):#constructor, with default values to params
        self.st_name = st_name      #name of stall
        self.desc = desc            #short description
        self.prep_time = prep_time  #average time needed to prepare and serve an item
        self.halal = halal          #variable to check whether halal or not
        self.menu1 = menu1          #variable to store the menu
        self.menu2 = menu2          #incase a separate breakfast/special menu exists
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.changeover_time = changeover_time #whenever the special menu comes into effect

    # Calculate Queue (Feature E)
    def check_queue(self, people):
        '''while True:
            try:
                people = int(input("Enter number people queueing : "))
                break
            except ValueError:
                print("error.Enter Again")'''

        time = float(people * self.prep_time)
        return time


def create_menu():  # to create the menu list by inputting the item
    while True:
        try:
            n = int(input("enter number of items in menu"))
            menu_list = []
            for i in range(0, n):
                menu_list.append(input_item())
            if n==0:
                pass

            return menu_list
        except:
            continue


def day_menu(): # to create the list of menus for different days of the week
    while True:
        try:
            menu_list = []
            for i in range(0, 7):  # day 0 starts sunday and saturday is day 6
                print("enter menu for day", i)
                menu_list.append(create_menu())
            return menu_list
        except:
            continue


def input_time():       # to create a list of times
    while True:
        try:
            time_list = []
            for i in range(0, 7):# day 0 starts sunday and saturday is day 6
                print("enter time for day", i)
                t = input("enter time in format xx xx")
                time_list = time_list + [t]
            return time_list
        except:
            continue


def check_halal():
    t = input("Enter t or T if stall is halal. otherwise enter anything")
    if t == "T" or t == "t":
        return True
    return False


def create_stall(): #function for enabling user input and creating the stall object
    st_name = input("Enter Stall name:")
    desc = input("enter Description")
    prep_time = float(input("Enter prep time in minutes"))
    menu1 = day_menu()
    print("enter opening Hours")
    opening_hrs = input_time()
    print("enter closing Hours")

    closing_hrs = input_time()
    chk = input("Is there a secondary menu?(Y or N")
    if chk == "y" or chk == "Y":
        menu2 = day_menu()
        print("enter changeover hours when the 2nd menu comes to effect (if there is none, enter 00 00")
        change_hrs = input_time()
    else:
        menu2 = []
        change_hrs = []
    halal = check_halal()
    stall_x = Stall(st_name, desc, prep_time, halal, menu1, menu2, opening_hrs, closing_hrs, change_hrs)
    return stall_x


def sort_data(db): # sorting data using linear sort
    for i in range(len(db)):
        for j in range(i, len(db)):
            if db[i].st_name.upper()[i] < db[j].st_name.upper()[i]:
                temp = db[i]
                db[i] = db[j]
                db[j] = temp


def Search_item(db, target): #search algorithm implemented using binary search.
    low = 0
    high = len(db) - 1
    while low <= high:
        mid = (low + high) // 2
        if db[mid].st_name.upper() == target.upper():
            return (True, mid)
        elif target.upper() < db[mid].st_name.upper():
            high = mid - 1
        else:
            low = mid + 1
    return (False, -1)


def make_db(): #function to create database
    n = int(input("enter number of items in database"))
    db = []
    for i in range(n):
        db.append(create_stall())
    sort_data(db)
    data_file = open("stall_info.out", mode="wb")       #data file object variable
    pickle.dump(db, data_file)                      #dumping(storing) the data in the file stall_info.out
    data_file.close()

def add_items(): # function to insert data into a database once created
    data_file = open("stall_info.out", mode="rb")
    db = pickle.load(data_file)
    data_file.close()
    n = int(input("enter number of items to add in database"))
    for i in range(n):
        db.append(create_stall())
    sort_data(db)
    data_file = open("stall_info.out", mode="wb")
    pickle.dump(db, data_file)
    data_file.close()


def print_db(): # test function, not important
    data_file = open("stall_info.out", mode="rb")
    db = pickle.load(data_file)
    data_file.close()
    for i in range(len(db)):
        print (db[i].st_name)
