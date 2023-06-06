# import click
from colorama import Fore, Back, Style, init
from tkinter.filedialog import askopenfile
from tkinter import *
from Hash import Hash
from P2H import P2H

class main:
    def __init__(self):
        self.HashSys = Hash() 
        self.P2HSys = P2H()
        print (Fore.YELLOW + '''
                               ______  _    _           _     
                              |  ____|| |  | |         | |    
                     _ __ ___ | |__   | |__| | __ _ ___| |__  
                    | '_ ` _ \|  __|  |  __  |/ _` / __| '_ \ 
                    | | | | | | |____ | |  | | (_| \__ \ | | |
                    |_| |_| |_|______||_|  |_|\__,_|___/_| |_|                      

                                          Created by SHemarati 
    __________________________________________________________________________\n'''+ Fore.RESET)

    def IseeHash(self):
        print(f"Searching text: ")

    def P2H(self):
        print(Fore.RED + "              ______Password List to Hash code_____\n" + Fore.RESET)
        self.P2HSys.test()

    def value(self):
        print (Fore.RED + "     _______Select Protocol Type_______\n")
        name  = 'value'
        self.Protocol(name)

    def Protocol(self , name):
        if name == 'value':
            Address = self.HashSys

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
                Address.sha256()
                break
            elif Protocol == '2' :
                Address.sha512()
                break
            elif Protocol == '3' :
                Address.sha3_256()
                break
            elif Protocol == '4' :
                Address.md5()
                break
            elif Protocol == '5' :
                Address.sha1()
                break
            elif Protocol == '6' :
                Address.blake2s()
                break
            elif Protocol == '7' :
                Address.whirlpool()
                break
            elif Protocol == '8' :
                Address.shake_128()
                break
            elif Protocol == '9' :
                Address.shake_256()
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

if __name__ == '__main__':
    my_main_instance = main()
    my_main_instance.StartUp()