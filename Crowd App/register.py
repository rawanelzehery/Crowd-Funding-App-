from input import *
from filehandler import *

def register():
    print("Register ")
    firstname = askforname("Plz Enter your First Name : ")
    lastname = askforname("Plz Enter your Last Name : ")
    Email = askforemail("Plz Enter your Email :")
    Passward = askforpass("Plz Enter your Passward")
    Confirm_Passward = askforpass("PLZ Confirm Your Passward ")
    phone_num = askforphone("Plz Enter Your Phone Number")
    ID = generatid()
    userinfo = f"{ID}:{Passward}:{firstname}:{lastname}:{Email}:{phone_num}\n"
    added = adduser(userinfo)
    if added :
        print("User Added Succesfully ")
    else:
        print("Unsuccessful Operation ")


