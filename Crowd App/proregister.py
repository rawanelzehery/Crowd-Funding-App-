from  projectinput import *
from projecthandler import *
def project():
    userid = checkid("Plz , Enter User ID")
    title = askfortitle("Enter Your Project TITLE : ")
    des = askfortitle("Enter Your Project Describtion : ")
    target =askfornum("PLZ , Enter Your Total  Target : ")
    proj_id = generatid()
    start_date =askfordate("Plz ,Enter The Start Date of Project ")
    end_date =askfordate("Plz ,Enter The End Date of Project ")
    #checked = checkdate(start_date,end_date)



    proj_info = f"{userid}:{proj_id}:{title}:{des}:{target}:{start_date}:{end_date}\n"
    added = addproj(proj_info)
    if added:
        print("Project Added Succesfully ")
    else:
        print("Unsuccessful Operation ")


