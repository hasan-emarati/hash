import click
from colorama import Fore, Back, Style, init
from tkinter.filedialog import askopenfile
from tkinter import *

class main:
    def __init__(self):
        print (Fore.YELLOW + '''
           ______  _    _           _     
          |  ____|| |  | |         | |    
 _ __ ___ | |__   | |__| | __ _ ___| |__  
| '_ ` _ \|  __|  |  __  |/ _` / __| '_ \ 
| | | | | | |____ | |  | | (_| \__ \ | | |
|_| |_| |_|______||_|  |_|\__,_|___/_| |_|                      
                        
                      Created by SHemarati 
________________________________________________________________\n'''+ Fore.RESET)
    def Search_In_Hash(self, text):
        print("Searching")

    def pass_List_To_Hash(self):
        print("Passing")

    def Val_To_Hash(self, Val):
        print("Val=")

if __name__ == '__main__':
    main()