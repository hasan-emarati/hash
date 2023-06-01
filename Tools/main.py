# import click
from colorama import Fore, Back, Style, init
from tkinter.filedialog import askopenfile
from tkinter import *
from Hash import Hash

class main:
    def __init__(self):
        HashSys = Hash 
        print (Fore.YELLOW + '''
           ______  _    _           _     
          |  ____|| |  | |         | |    
 _ __ ___ | |__   | |__| | __ _ ___| |__  
| '_ ` _ \|  __|  |  __  |/ _` / __| '_ \ 
| | | | | | |____ | |  | | (_| \__ \ | | |
|_| |_| |_|______||_|  |_|\__,_|___/_| |_|                      
                        
                      Created by SHemarati 
________________________________________________________________\n'''+ Fore.RESET)

    def IseeHash(self):
        print(f"Searching text: ")

    def P2H(self):
        """
        Translate password list to hash.
        """

    def value(self):
        Val = input(Fore.LIGHTBLUE_EX + "Enter Your Value >>> ")
        self.Protocol()
        return Val

    def Protocol(self):
        while True:
            print(Fore.YELLOW + "Place Select Your Protocol You Have a Some Protocol : ")
            print('''
[1] > sha256     SHA-256 is a cryptographic hashing
[2] > sha512     SHA-512 is a cryptographic hash function 
[3] > sha3_256   SHA3-256 is a cryptographic hash function that takes an input data a
[4] > md5        MD5 is a cryptographic hash function that produces a fixed-size outpu
[5] > sha1       SHA-1: A cryptographic 
[6] > blake2s    BLAKE2s is a fast and secure cryptographic hash f
[7] > whirlpool
[8] > shake_128  SHAKE128 is a fast and secure cryptographic hash function that can produce
[9] > shake_256  SHAKE256 is a cryptographic hash function that produces a variable-length output of h
            ''' + Fore.RESET)
            Protocol = input(Fore.LIGHTBLUE_EX + "Enter Your Protocol Number >>> ")
            if Protocol == '1' :
                Hash.sha256()
                break
            elif Protocol == '2' :
                Hash.sha512()
                break
            elif Protocol == '3' :
                Hash.sha3_256()
                break
            elif Protocol == '4' :
                Hash.md5()
                break
            elif Protocol == '5' :
                Hash.sha1()
                break
            elif Protocol == '6' :
                Hash.blake2s()
                break
            elif Protocol == '7' :
                Hash.whirlpool()
                break
            elif Protocol == '8' :
                Hash.shake_128()
                break
            elif Protocol == '9' :
                Hash.shake_256()
                break
            else :
                print(Fore.RED + "Invalid Protocol: " + Protocol + "\nPlease Enter the new Value" + Fore.RESET)


    def StartUp(self):
        print (Fore.RED + "                 Welcome to the mE Hash" + Fore.RESET)
        while True :
            print(Fore.YELLOW + '''
            [1]  > p2h        Transelate the Password List to Hash Code  
            [2]  > Value      Conversion Value to Hash Code
            [3]  > IseeHash   Search in the Hash Library For Find Password
            ''' + Fore.RESET)
            InMode = input(Fore.LIGHTBLUE_EX + "Enter Your System Mode >>> ")
            if InMode == '1' :
                self.P2H()
                break
            elif InMode == '2' :
                self.value()
                break
            elif InMode == '3' :
                self.IseeHash()
                break
            else :
                print(Fore.RED + "Invalid InMode: " + InMode)
                print("Please enter Your new Value" + Fore.RESET)

    def UI(self):
        try:
            path = askopenfile(initialdir="/", title="Select file",
                        filetypes=(("txt files", "*.txt"),("all files", "*.*")))
            PassWord_List = path.read()
            print (Fore.GREEN + "File selected" + Fore.RESET)
        except:
            print (Fore.RED + "UI Error" + Fore.RESET)

    def Prompt(self):
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

    def UandP(self):

        while True :
            print(Fore.CYAN + "[1] UI Select File")
            print(Fore.CYAN + "[2] Prompt Select File")
            choice = input(Fore.BLUE + 'Please select > ' + Fore.RESET)
            if choice == '1':
                self.UI()
                break
            elif choice == '2':
                self.Prompt()
                break
            else:
                print(Fore.RED + 'Invalid choice, please try again' + Fore.RESET)
        
if __name__ == '__main__':
    my_main_instance = main()
    my_main_instance.StartUp()