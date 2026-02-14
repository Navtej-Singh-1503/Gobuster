
'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

14/02/2026

Version - 0.1.2

mail - navtejsingh15032011@gmail.com

'''

import os
from FILES.brand import intro
import time
from FILES.color import *
import subprocess
import sys


os.system("clear")


print(RED+"")
print(intro)


result = subprocess.run([sys.executable, "-m", "pip", "show", "aiohttp"], capture_output=True, text=True)


print(GREEN+"["+RED+"!"+GREEN+"]"+RESET+"NEED TO INSTALL SOME PACKAGES")
print(GREEN+"["+RED+"!"+GREEN+"]"+RESET+"PROCESS WILL START IN 3 SECONDS")
time.sleep(3)
print(GREEN+"["+RED+"*"+GREEN+"]"+RESET+"PROCESS STARTED")
os.system("sudo apt update")



if result.returncode != 0:

    os.system("pip install aiohttp")


print(GREEN+"["+RED+"+"+GREEN+"]"+RESET+"PROCESS COMPLETED NOW YOU CAN START RUNING gobuster.py")
