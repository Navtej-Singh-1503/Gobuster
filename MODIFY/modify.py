
'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

14/02/2026

version - 0.2.1

mail - navtejsingh15032011@gmail.com

'''

from FILES.color import *
from FILES.brand import intro
import os
import shutil
from pathlib import Path

os.system('clear')

print(RED + "")
print(intro)
print(GREEN + "                                   -By Navtej-Singh-1503")
print(GREEN + "                                   -Contact navtejsingh15032011@gmail.com")

print(GREEN+"["+RED+"1"+GREEN+"]"+RESET+" CHANGE SECLIST")
print(GREEN+"["+RED+"2"+GREEN+"]"+RESET+" UPDATE")

print("")

user = input("==========>>  ")

if user == "1":
    sec_list_path = input(GREEN+"["+RED+"*"+GREEN+"]"+RESET+" ENTER PATH TO YOUR SECLIST FILE\n==>> ")

    try:
        data_folder = Path("..") / "DATA"
        target_file = data_folder / "backdoor_list.txt"


        if target_file.exists():
            target_file.unlink()


        shutil.move(sec_list_path, target_file)

        print(GREEN+"["+RED+"+"+GREEN+"]"+RESET+"Seclist Updated Successfully!")

    except Exception as e:
        print(GREEN+"["+RED+"!"+GREEN+"]"+RESET+" Error:", e)


elif user == "2":
    result = os.system("git pull")
    if result == 0:
        print(GREEN+"["+RED+"+"+GREEN+"]"+RESET+ " Tool Updated Successfully!")
    else:
        print(GREEN+"["+RED+"!"+GREEN+"]"+RESET+" Update Failed!")



else:
    print(GREEN+"["+RED+"!"+GREEN+"]"+RESET+" INVAILD INPUT!!")
