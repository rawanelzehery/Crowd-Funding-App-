from projectinput import *
from projecthandler import *
from proregister import *

def projectdel():
    userid = askforintid("PLZ ,ENTER USER OF PROJECT ID : ")
    proj_id = askforintid("PLZ ,ENTER PROJECT ID : ")
    found = searchprojid(userid,proj_id)
    if found:
        print("Found User")
        print(found)
        deleted = deletefromprojects(found[1])
        if deleted:
            print("Project Deleted Successfully ")

    else:
        print("Project not Found")
        return projectdel()

#projectdel()


def projectedit():
    userid = askforintid("PLZ ,ENTER USER OF PROJECT ID : ")
    proj_id = askforintid("PLZ ,ENTER PROJECT ID : ")
    found = searchprojid(userid, proj_id)

    if found:
        print("Found User")
        print(found)
        updated = deletefromprojects(found[1])
        if updated:
            print("Project Deleted Successfully ")
            project()

    else:
        print("Project not Found")
        return projectedit()

#projectedit()