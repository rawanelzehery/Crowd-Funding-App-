from filehandler import *

def addproj(proinfo):
    try:
        file = open("projects.txt","a")
    except:
        print("couldn't open")
        return False
    else:
        file.write(proinfo)
        return True
        file.close


def checkid (messag):
    usrid = input(messag)
    found = searchuserid(usrid)
    if found:
        print("Found")
        return usrid

    else:
        print("Not Found")
        return checkid(messag)


def veiwprojects():
    try:
        fileobj=  open("projects.txt","r")

    except:
        return False
        print("Can't Open File ")

    else:
        projects = fileobj.readlines()
        return projects


def writetoprojects(projectlist):
    try:
        file = open("projects.txt", "w")
    except:
        return False
    else:
        for pro in projectlist:

            file.write(pro)

    return True


def searchprojid(usrid,projid):
    allprojects = veiwprojects()
    for pro in allprojects:

        pro_info = pro.strip("\n")
        pro_info = pro.split(":")
        if pro_info[0] == usrid and pro_info[1] == projid:
            pro_index = allprojects.index(pro)
            return True,pro_index
    else:
        return False

#x =searchprojid("1669731304","1669894893")
#print(x)
def deletefromprojects(indx):
    allprojects = veiwprojects()
    del allprojects[indx]
    deleted = writetoprojects(allprojects)
    return deleted

#y=deletefromprojects(0)
#print(y)