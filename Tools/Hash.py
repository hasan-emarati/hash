import hashlib

class Hash:
    def __init__(self):
        self.text = "U".encode('utf-8')

    def sha256(self):
        Hash_Object = hashlib.sha256(self.text)
        Hex_Dig = Hash_Object.hexdigest()
        print(Hex_Dig) 

    def sha512(self):
        Hash_Object = hashlib.sha512(self.text)
        Hex_Dig = Hash_Object.hexdigest()
        print(Hex_Dig)

    def sha3_256(self):
        hash_object = hashlib.sha3_256(self.text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig) 

    def md5(self): 
        hash_object = hashlib.md5(self.text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    
    def sha1(self):
        hash_object = hashlib.sha1(self.text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    def blake2s(self):
        hash_object = hashlib.blake2s(self.text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    def whirlpool(self):
        hash_object = hashlib.new('whirlpool', self.text)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    def shake_128(self):
        hash_object = hashlib.shake_128(self.text)
        hex_dig = hash_object.hexdigest(16)
        print(hex_dig)
    
    def shake_256(self):
        hash_object = hashlib.shake_256(self.text)
        hex_dig = hash_object.hexdigest(16)
        print(hex_dig)

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