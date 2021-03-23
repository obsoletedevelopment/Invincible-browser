import time
import webbrowser
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
    print("1 = basic browse")
    print("2 = last opened")
    print("3 = history")
    print("4 = history")
    print("5 = quit")
    print("")
    choice = input("enter an option: ")
    if choice == "1":
        browse()
    elif choice == "2":
        lastopened()
    elif choice == "3":
        history()
    elif choice == "4":
        thebigone()
    elif choice == "5":
        quit()
    else:
        menu()

#web search

def browse():
    print("")
    website = input("enter website URL")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # Go to website input
    webbrowser.get(chrome_path).open(website)

    f = open("lastopened.txt", "w")
    f.write(website)
    f.close()

    a = open("history.txt", "a")
    a.write(website + "-----")
    a.close()

    menu()

def lastopened():
    f = open("lastopened.txt", "r")
    webbrowser.open(f.read())  # Go to website input
    menu()

def 
def history():
    f = open("history.txt", "r")
    print("")
    print(f.read())
    print("")
    menu()

def credits():
    print("everything: obsolete dev")

def secretmode():
    print("")
    print("welcome to debugmode i use this for new unreleased features")
    print("")
    print("1 = big gunz mode (once tab is closed it reopens it")
    print("")
    choice = input("enter an option")
    if choice == "1":
        menu()
    else:
        menu()
menu()
