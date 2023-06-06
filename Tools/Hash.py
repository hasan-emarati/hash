import hashlib
from colorama import Fore

class Hash:
    def value(self):
        InValue = input(Fore.LIGHTBLUE_EX + "Enter Your Value >>> ")
        Value = f'{InValue}'.encode('utf-8')
        return Value , InValue

    def sha256(self):
        Value = self.value()
        self.text = Value[0]
        Hash_Object = hashlib.sha256(self.text)
        Hex_Dig = Hash_Object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET) 

    def sha512(self):
        Value = self.value()
        self.text = Value[0]
        Hash_Object = hashlib.sha512(self.text)
        Hex_Dig = Hash_Object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)

    def sha3_256(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.sha3_256(self.text)
        Hex_Dig = hash_object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET) 

    def md5(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.md5(self.text)
        Hex_Dig = hash_object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)
    
    def sha1(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.sha1(self.text)
        Hex_Dig = hash_object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)

    def blake2s(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.blake2s(self.text)
        Hex_Dig = hash_object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)

    def whirlpool(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.new('whirlpool', self.text)
        Hex_Dig = hash_object.hexdigest()
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)

    def shake_128(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.shake_128(self.text)
        Hex_Dig = hash_object.hexdigest(16)
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)
    
    def shake_256(self):
        Value = self.value()
        self.text = Value[0]
        hash_object = hashlib.shake_256(self.text)
        Hex_Dig = hash_object.hexdigest(16)
        print(Fore.MAGENTA + f"{Value[1]} : " + Fore.GREEN + f'{Hex_Dig}' + Fore.RESET)

if __name__ == '__main__':
    Run = Hash()
    # Run.sha256()
    # Run.sha512()
    # Run.sha3_256()
    # Run.md5()
    # Run.sha1()
    # Run.blake2s()
    # Run.whirlpool()
    # Run.shake_128()
    # Run.shake_256()