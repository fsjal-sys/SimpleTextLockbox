import os, ast
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generateKey(password):
    #Returns unique bytes object key from string password input
    with open('resources/salt.txt','rb') as f:
        salt = f.read()
    encodedPassword = password.encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return kdf.derive(encodedPassword)

def lock(key, plainText):
    #Takes key and string plain text to return AES encrypted cipher text
    #Initialization vector (IV) and encryption tag are prepended to cipher text
    plainText = plainText.encode()
    IV = os.urandom(12)
    encryptor = Cipher(algorithms.AES(key), modes.GCM(IV)).encryptor()
    cipherText = encryptor.update(plainText) + encryptor.finalize()
    cipherText = IV + bytes("ᚨ",'utf-8') + encryptor.tag + bytes("ᚨ",'utf-8') + cipherText
    return cipherText

def unlock(key, cipherText):
    #Takes key and cipher text and performs decryption to return plain text
    splitted = ast.literal_eval(cipherText).split(bytes("ᚨ", 'utf-8'), 2)
    IV = splitted[0]
    tag = splitted[1]
    cipherText = splitted[2]
    decryptor = Cipher(algorithms.AES(key), modes.GCM(IV, tag)).decryptor()
    plainText = decryptor.update(cipherText) + decryptor.finalize()
    return plainText.decode()

