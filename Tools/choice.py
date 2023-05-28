# Created by SHemarati
from colorama import Fore, Back, Style, init
from tkinter.filedialog import askopenfile
from tkinter import *

class choice:
    print (Fore.YELLOW + '''
           ______  _    _           _     
          |  ____|| |  | |         | |    
 _ __ ___ | |__   | |__| | __ _ ___| |__  
| '_ ` _ \|  __|  |  __  |/ _` / __| '_ \ 
| | | | | | |____ | |  | | (_| \__ \ | | |
|_| |_| |_|______||_|  |_|\__,_|___/_| |_|                      
                        
                        Created by SHemarati                 
        '''+ Fore.RESET)   
    
    def UI():
        try:
            path = askopenfile(initialdir="/", title="Select file",
                        filetypes=(("txt files", "*.txt"),("all files", "*.*")))
            PassWord_List = path.read()
            print (Fore.GREEN + "File selected" + Fore.RESET)
        except:
            print (Fore.RED + "UI Error" + Fore.RESET)

    def Prompt():
        try:
            print (Fore.MAGENTA + "\t\tType File \"*.txt\"\n")
            Path = input("Enter Your Directory ==>  " + Fore.RESET)
            if Path[-3:] == 'txt':
                Open = open(Path , "r")
                PassWord_List = Open.read()
                print (Fore.GREEN + "File selected" + Fore.RESET)
                return PassWord_List
            else :
                print (Fore.RED + "Invalid File" + Fore.RESET)
        except:
            print (Fore.RED + "Prompt Error" + Fore.RESET)

    while True :
        print(Fore.CYAN + "[1] UI Select File")
        print(Fore.CYAN + "[2] Prompt Select File")
        choice = input(Fore.BLUE + 'Please select > ' + Fore.RESET)
        if choice == '1':
            UI()
            break
        elif choice == '2':
            Prompt()
            break
        else:
            print(Fore.RED + 'Invalid choice, please try again' + Fore.RESET)

if __name__ == '__main__':
    choice()
# Created by SHemarati