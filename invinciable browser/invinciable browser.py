import time
import webbrowser
import os
#prints load screen


print(""" _            _            _ _     _       
(_)          (_)          (_) |   | |      
 _ _ ____   ___ _ __   ___ _| |__ | | ___  
| | '_ \ \ / / | '_ \ / __| | '_ \| |/ _ \ 
| | | | \ V /| | | | | (__| | |_) | |  __/ 
|_|_| |_|\_/ |_|_| |_|\___|_|_.__/|_|\___|  """)
print("by obsolete_dev")
print("ver: 0.01 beta")
#main menu

def menu():
    print("")
    print("1 = load browser")
    print("2 = quit")
    print("")
    choice = input("enter an option: ")
    if choice == "1":
        browse()
    elif choice == "2":
        quit()
    else:
        menu()

#web search

def browse():
    print("")
    os.startfile("browser-custom.exe")
    menu()

menu()
