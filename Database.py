import datetime
days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
}

class Menu:
    def __init__(self,fname,price,day):
        self.food_name = fname
        self.price =price
        self.days_available= day
    food_name =""
    price =0
    days_available =[]

class Store:
    def __init__(self,sname,food,opening,closing):
        self.store_name = sname
        self.food_items = food
        self.opening_time =opening
        self.closing_time = closing
    store_name = ""
    food_items =[]
    opening_time = datetime.time(0,0,0)
    closing_time = datetime.time(0,0,0)
