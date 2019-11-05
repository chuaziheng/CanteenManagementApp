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
    n = int(input("enter number of items in menu"))
    menu_list = []
    for i in range(0, n):
        menu_list = menu_list+ [input_item()]
    return menu_list


def day_menu():
    menu_list = []
    for i in range(0, 7):  # day 0 starts sunday and saturday is day 6
        print("enter menu for day", i)
        menu_list = menu_list + create_menu()
    return menu_list


def input_time():
    time_list = []
    for i in range(0, 7):
        print("enter time for day", i)
        t = input("enter time in format xx xx")
        time_list=time_list+[t]
    return time_list


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
    menu2 = day_menu()
    print("enter opening Hours")
    opening_hrs = input_time()
    print("enter closing Hours")
    closing_hrs = input_time()
    print("enter changeover hours(if there is none, enter 00 00")
    change_hrs = input_time()
    halal = check_halal()
    stall_x = Stall(st_name, desc, prep_time, halal, menu1, menu2, opening_hrs, closing_hrs, change_hrs)
    return stall_x


def make_db():
    n = int(input("enter number of items in database"))
    db = []
    for i in range(n):
        db= db+[create_stall()]

    data_file = open("stall_info.out", mode="wb")
    pickle.dump(db, data_file)
    data_file.close()

def print_db():
    data_file = open("stall_info.out", mode="rb")
    db= pickle.load( data_file)
    data_file.close()
    print (db[0].st_name)


print_db()
