import time
import re
def askforname(message):
    name = input(message)
    if name.isalpha():
        return name
    else:
        return askforname(message)


def generatid():
    id = int(time.time())
    return id


def askforemail(messege):
    email = input(messege)
    #pattern = (r'/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/')
    #if (re.fullmatch(pattern, email)):
    if "@" and ".com"  in email:
        return email
    else:
        print("Invalid Email")
        askforemail(messege)

def askforphone(message):
    phone = input(message)

    if phone[:3] == "+20" or len(phone) == 13 :
        return phone
    else:
        print("Invalid phone number ")
        return askforphone(message)

def askforpass(message):
    pas = input(message)
    #pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    #if (re.fullmatch(pattern, pas)):
    if len(pas) >= 8 :
        return pas
    else:
        print("Invalid password ")
        return askforpass(message)


def conformpass(num1,num2):
    if num1 == num2 :
        print("Strong Passward ")
        return True
    else:
        print("not confirmed passward")
        return askforpass("Enter The Passward Again")


def askforintid(message):
    num = input(message)
    if num.isdigit():
        return num
    else:
        return askforintid(message)



