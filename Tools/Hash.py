import hashlib

class Hash:
    def __init__(self):
        self.text = "U".encode('utf-8')

    @staticmethod
    def sha256():
        Hash_Object = hashlib.sha256(Hash().text)
        Hex_Dig = Hash_Object.hexdigest()
        print(Hex_Dig) 

    @staticmethod
    def sha512():
        Hash_Object = hashlib.sha512(Hash().text)
        Hex_Dig = Hash_Object.hexdigest()
        print(Hex_Dig)

    @staticmethod
    def sha3_256():
        hash_object = hashlib.sha3_256(Hash().text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig) 

    @staticmethod
    def md5(): 
        hash_object = hashlib.md5(Hash().text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    
    @staticmethod
    def sha1():
        hash_object = hashlib.sha1(Hash().text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    @staticmethod
    def blake2s():
        hash_object = hashlib.blake2s(Hash().text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    @staticmethod
    def whirlpool():
        hash_object = hashlib.new('whirlpool', Hash().text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    @staticmethod
    def shake_128():
        hash_object = hashlib.shake_128(Hash().text)
        hex_dig = hash_object.hexdigest(16)
        print(hex_dig)
    
    @staticmethod
    def shake_256():
        hash_object = hashlib.shake_256(Hash().text)
        hex_dig = hash_object.hexdigest(16)
        print(hex_dig)

if __name__ == '__main__':
    Hash()
    # Hash.sha256()
    # Hash.sha512()
    # Hash.sha3_256()
    # Hash.md5()
    # Hash.sha1()
    # Hash.blake2s()
    # Hash.whirlpool()
    # Hash.shake_128()
    # Hash.shake_256()