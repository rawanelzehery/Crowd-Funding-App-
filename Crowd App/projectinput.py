import  time
import re
from datetime import datetime
def askfortitle(message):
    name = input(message)
    if name.isalpha():
        return name
    else:
        return askfortitle(message)


def generatid():
    id = int(time.time())
    return id


def askfornum(message):
    num = input(message)
    if num.isdigit():
        return num
    else:
        return askfornum(message)

def askfordate(message):
    date = input(message)
    format = "%d-%m-%Y"
    res = bool(datetime.strptime(date, format))
    if res:
        return date
    else:
        return askfordate(message)

def askforintid(message):
    num = input(message)
    if num.isdigit():
        return num
    else:
        return askforintid(message)

def checkdate(date1,date2):


    datenow = datetime.today()
    if date1 <= date2 and date1 > datenow:

        return True

    else:

        return False

checkdate(22-12-2022,23-12-2024)