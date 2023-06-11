def adduser(userinfo):
    try:
        file = open("user.txt","a")
    except:
        print("couldn't open")
        return False
    else:
        file.write(userinfo)
        return True


def writeiuserinfile(userlist):
    try:
        file = open("user.txt","w")
    except:
        return False
    else:
        for user in userlist:
            file.write(user)

        return True


def getallusers():
    try:
        fileobj=  open("user.txt","r")

    except:
        return False
        print("Can't Open File ")

    else:
        users = fileobj.readlines()
        return users

def searchaboutuser(userid):
    allusers = getallusers()
    for user in allusers:

        user_info = user.strip("\n")
        user_info = user.split(":")
        if user_info[0] == userid:
            user_index = allusers.index(user)
            return True , user_index
    else:
        return False

def deletefromfile(index):
    allusers = getallusers()
    del allusers[index]
    deleted = writeiuserinfile(allusers)
    return deleted



def searchuser(pas):
    allusers = getallusers()
    for user in allusers:
        user_info = user.strip("\n")
        user_info = user.split(":")

        print(user_info[1])
        if user_info[1] == pas:
            #user_index = allusers.index(user)
            return True
    else:
        return False


def checkuser(Pas):
    allusers = getallusers()
    for user in allusers:
        user_info = user.strip("\n")
        user_info = user.split(":")
        if user_info[1] == Pas  :
            print("Found")
            return True
        else:
            return False



def searchuserid(userid):
    allusers = getallusers()
    for user in allusers:

        user_info = user.strip("\n")
        user_info = user.split(":")
        if user_info[0] == userid:
            user_index = allusers.index(user)
            return True
    else:
        return False
