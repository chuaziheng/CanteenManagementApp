import pickle


class item:
    def __init__(self, item_name="", price=0.0):
        self.item_name = item_name
        self.price = price


def input_item():
    item_name = input("Enter item name")
    item_price = float(input("enter item price"))
    return item(item_name, item_price)


class Stall:
    def __init__(self, st_name="", desc="", prep_time=0.0, halal=False, menu1=[], menu2=[], opening_time=[],
                 closing_time=[], changeover_time=[]):
        self.st_name = st_name
        self.desc = desc
        self.prep_time = prep_time
        self.halal = halal
        self.menu1 = menu1
        self.menu2 = menu2
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.changeover_time = changeover_time


def create_menu():
    while True:
        try:
            n = int(input("enter number of items in menu"))
            menu_list = []
            for i in range(0, n):
                menu_list = menu_list + [input_item()]
            return menu_list
        except:
            continue


def day_menu():
    while True:
        try:
            menu_list = []
            for i in range(0, 7):  # day 0 starts sunday and saturday is day 6
                print("enter menu for day", i)
                menu_list = menu_list + create_menu()
            return menu_list
        except:
            continue


def input_time():
    while True:
        try:
            time_list = []
            for i in range(0, 7):
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


def create_stall():
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


def sort_data(db):
    for i in range(len(db)):
        for j in range(i, len(db)):
            if db[i].st_name.upper()[i] < db[j].st_name.upper()[i]:
                temp = db[i]
                db[i] = db[j]
                db[j] = temp


def Search_item(db, target):
    low = 0
    high = len(db) - 1
    while low <= high:
        mid = (low + high) // 2
        if db[mid].st_name.upper() == target.upper():
            return True
        elif target.upper() < db[mid].st_name.upper():
            high = mid - 1
        else:
            low = mid + 1
    return False


def make_db():
    n = int(input("enter number of items in database"))
    db = []
    for i in range(n):
        db = db + [create_stall()]
    sort_data(db)
    data_file = open("stall_info.out", mode="wb")
    pickle.dump(db, data_file)
    data_file.close()


def print_db():
    data_file = open("stall_info.out", mode="rb")
    db = pickle.load(data_file)
    data_file.close()
    sort_data(db)
    print(Search_item(db, "Mc Donalds"))

    print(" sort_successful")


