from hashlib import sha256 , sha512 , sha3_256 , md5 , sha1 , blake2s

class Hash:
    def Sha256():
        Passwords = "U".encode('utf-8')
        Hash_Object = sha256(Passwords)
        Hex_Dig = Hash_Object.hexdigest()
        print(Hex_Dig) 
      

    def Sha512():
        Passwords = "U".encode('utf-8')
        Hash_Object = sha512(Passwords)
        Hex_Dig = Hash_Object.hexdigest()
        print(Hex_Dig)

    def Sha3_256():
        text = 'U'
        hash_object = sha3_256(text.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        print(hex_dig) 

    def MD5(): 
        text = 'U'
        hash_object = md5(text.encode())
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    
    def sha_1():
        text = 'U'
        hash_object = sha1(text.encode())
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

    def BLAKE2():
        text = 'U'
        hash_object = blake2s(text.encode())
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

if __name__ == '__main__':
    Hash()