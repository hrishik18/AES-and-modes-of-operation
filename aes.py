import pyaes
import pbkdf2
import binascii
import os
import secrets


def ECB():
    print("-----------------------ECB--------------------------")
    print('AES encryption key:', binascii.hexlify(key))
    aes = pyaes.AESModeOfOperationECB(key)
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted:', binascii.hexlify(ciphertext))
    aes = pyaes.AESModeOfOperationECB(key)
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted:', decrypted)
    print("----------------------------------------------------")


def CBC():
    print("-----------------------CBC--------------------------")
    print('AES encryption key:', binascii.hexlify(key))
    aes = pyaes.AESModeOfOperationCBC(key, iv=iv)
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted:', binascii.hexlify(ciphertext))
    aes = pyaes.AESModeOfOperationCBC(key, iv=iv)
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted:', decrypted)
    print("----------------------------------------------------")


def CFB():

    print("-----------------------CFB--------------------------")
    print('AES encryption key:', binascii.hexlify(key))
    aes = pyaes.AESModeOfOperationCFB(key, iv=iv, segment_size=8)
    str1 = "encrypt!"
    str2 = ""
    for x in str1:
        if x != " ":
            str2 += x+" "
    str2 = str2[:-1]
    plx = str2.split(" ")
    ciphertext = aes.encrypt(plx)
    print('Encrypted:', binascii.hexlify(ciphertext))
    aes = pyaes.AESModeOfOperationCFB(key, iv=iv, segment_size=8)
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted:', decrypted)
    print("----------------------------------------------------")


def OFB():
    print("-----------------------OFB--------------------------")
    print('AES encryption key:', binascii.hexlify(key))
    aes = pyaes.AESModeOfOperationOFB(key, iv=iv)
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted:', binascii.hexlify(ciphertext))
    aes = pyaes.AESModeOfOperationOFB(key, iv=iv)
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted:', decrypted)
    print("----------------------------------------------------")


password = "secret"
passwordSalt = os.urandom(16)

key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key))
iv = "InitializationVe"

plaintext = "Text for encrypt"
args = int(10)
while(args != 0):
    print("1.ECB")
    print("2.CBC")
    print("3.CFB")
    print("4.OFB")
    print("0.Exit")
    print()
    a = int(input("Enter your choice\n"))
    if a == 1:
        ECB()
    elif a == 2:
        CBC()
    elif a == 3:
        CFB()
    elif a == 4:
        OFB()
    elif a == 0:
        break
    else:
        print("Wrong input!!")
