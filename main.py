from csv import reader
from hashlib import sha256
from hashlib import blake2b, blake2s
from colorama import Fore, Back, Style, init
import random


key2val = {}

print('value to hash [1] ')
print('search hash Library [2] ')
print('value list to hash [3] ')
Qmode = input('select mode : ')



def Password_to_hash():
    print('[1] : sha256 ')
    print('[2] : blake2b ')
    QHash_mode = input('select hash mode : ')

    if QHash_mode == '1' :
        Qval_sha256 = input('Enter your value : ')
        hash_Enter_Password_sha256 = sha256(b"%s" % (Qval_sha256)).hexdigest()
        print('your hash value : ' , hash_Enter_Password_sha256)
    
    if QHash_mode == '2':
        Qval_blake2b = input('Enter your password : ')
        hash_Enter_Password_blake2b = blake2b(b'%s' % Qval_blake2b).hexdigest()
        print('your hash value : ' , hash_Enter_Password_blake2b)

if Qmode == '1':
    Password_to_hash()