def print_menu():
    choice = 0
    while choice < 1 or choice > 5:
        print("Welcome to Canteen A North Spine Information System!")
        print("\n")
        print("Menu : \n1. Stall Info \n2.Current Stalls \n3. Check Stalls on Date\n4. Operating Hours\n5. Check Queue")
        choice = int(input("\nEnter your Choice : "))
    return choice

def display_stall(name) :
    choice = 0
    while choice < 1 or choice > 4:
        print(name)
        print("\n1. Menu\n2. Operating Hours\n3. Queue\n4. Menu on Date")
        choice = int(input("\nEnter your Choice : "))

print_menu()

  


