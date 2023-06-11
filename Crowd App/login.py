from filehandler import *
from projectentry import MainProject
def login():

    Passwrd = input("Enter Passward")
    found = searchuser(Passwrd)
    print(Passwrd)

    if found:
        print("Found User")
        print(found)
        print("Welcome User")
        MainProject()

    else:
        print("Can't Login ,Plz Register")
        return login()


