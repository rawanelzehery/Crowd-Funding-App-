from login import *
from crud import *
from register import *

def MainMenu ():

    choice = input("Please Enter r for Regisre , l for Login , d for delete user, x for exist ")
    if (choice == "r"):
        register()

    elif choice == 'l':
        login()

    elif choice == "u":
        updateuser()

    elif choice == "d":
        userdel()

    elif choice =="x":
        exit()

    else:
        print("Please Enter A valid Choice ")
    return MainMenu()



MainMenu()