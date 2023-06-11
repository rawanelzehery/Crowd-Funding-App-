from proregister import *
from projecthandler import *
from procrud import *

def MainProject():

    choice = input("Please Enter v for veiw all , d for delete  project, x for exist ,S for Search , E for Update ")
    if choice == "r":
        project()

    elif choice == "v":

        pro = veiwprojects()
        print(pro)

    elif choice == "d":
        projectdel()

    elif choice == "e":
        projectedit()


    elif choice == "x":
        exit()

    return MainProject()


#MainProject()

