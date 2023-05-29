import click
from colorama import Fore, Back, Style, init
from tkinter.filedialog import askopenfile
from tkinter import *

class main:
    @click.group()
    def cli():
        pass
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
    @cli.command()
    def IseeHash():
        click.echo('search in hash is running')
        print(f"Searching text: ")

    @cli.command()
    def P2H():
        """
        Translate password list to hash.
        """
        click.echo("Translating password list to hash...")

    @cli.command()
    def value():
        Val = input(Fore.LIGHTBLUE_EX + "Enter Your Value >>> ")
        

    cli.add_command(IseeHash)
    cli.add_command(P2H)
    cli.add_command(value)

    def Protocol():
        while True:
            print(Fore.YELLOW + "Place Select Your Protocol You Have a Some Protocol : ")
            print('''
            [1] > sha256        SHA-256 is a cryptographic hashing algorithm that produces a 256-bit (32-byte) hash value for a given input, widely used for digital signatures and encryption.  
            [2] > sha512        SHA-512 is a cryptographic hash function that produces a unique fixed-size output (512 bits) from an input data, commonly used for data integrity and security purposes.
            [3] > sha3_256      SHA3-256 is a cryptographic hash function that takes an input data and produces a fixed-size output of 256 bits, providing secure hashing and data integrity verification for various applications.
            [4] > md5           MD5 is a cryptographic hash function that produces a fixed-size output of 128 bits from an input data, but due to its vulnerabilities, it is no longer considered secure for cryptographic purposes.
            [5] > sha1          SHA-1: A cryptographic hash function that produces a fixed-size output of 160 bits, but is no longer considered secure for cryptographic applications.
            [6] > blake2s       BLAKE2s is a fast and secure cryptographic hash function that produces a fixed-size output of up to 256 bits, commonly used for data integrity and privacy-preserving protocols.
            [7] > whirlpool
            [8] > shake_128     SHAKE128 is a fast and secure cryptographic hash function that can produce a variable-length output of high quality, suitable for various applications such as key derivation and message authentication.
            [9] > shake_256     SHAKE256 is a cryptographic hash function that produces a variable-length output of high quality, based on the SHA-3 family, and is suitable for various applications such as key derivation and digital signatures.
            ''' + Fore.RESET)
            Protocol = input(Fore.LIGHTBLUE_EX + "Enter Your Protocol Number >>> ")
        
if __name__ == '__main__':
    main()
    main.cli()