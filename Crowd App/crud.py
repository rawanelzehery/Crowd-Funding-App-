from input import *
from filehandler import *
from register import *
def userdel():
    id = askforintid("PLZ Enter The User ID")
    found = searchaboutuser(id)
    if found :
        print("Found User")
        print(found)
        deleted = deletefromfile(found[1])
        if deleted:
            print("User Deleted Successfully ")

    else:
        print("User not Found")
        return userdel()


def updateuser():
    id = askforintid("PLZ Enter The User ID")
    found = searchaboutuser(id)
    if found:
        print("Found User")
        print(found)
        updated = deletefromfile(found[1])
        if updated:
            print("User delted add new one")
            register()

    else:
        print("User Not Found")
        return updateuser()