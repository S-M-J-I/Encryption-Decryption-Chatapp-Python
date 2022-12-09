import encrypt
import hill
import playfair
import otp
import railfence
import columnar
import DES
import decryptDES
import rsa
import RC4

publicKey, privateKey = rsa.newkeys(512)
cipherType = ""
plaint = " "
encMessage = ""
otp_msg = otp.otpmsg


def set_cipher_type(type):
    global cipherType
    cipherType = type
    print("Cipher is now :", cipherType)


def get_cipher_type():
    global cipherType
    return cipherType


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


"""
extract the option from a list and pass it through the 3rd argument
"""


def encryption(text, s, cipher=cipherType):
    plaintext = text
    global plaint
    global encMessage
    plaint = plaintext
    global cipherType
    cipherType = cipher

    print("encrypt func => Cipher is: ", cipherType)

    if(cipherType == "hill"):
        return hill.HillCipher(text, s)
        """
        execute cypher encryption here
        """
        pass
    elif(cipherType == "ceaser"):
        return encrypt.encryptceaser(text, s)
    elif(cipherType == "mono"):
        return encrypt.encryptmono(text)
        pass
    elif(cipherType == "playfair"):
        return playfair.encryptByPlayfairCipher(text, s)
    elif(cipherType == "otp"):
        return text
    elif(cipherType == "railfence"):
        return railfence.encryptRailFence(text, int(s))
    elif(cipherType == "polyalpha"):
        return encrypt.cipherpolyalphabetic(text, s)
    elif(cipherType == "columnar"):
        return columnar.encryptMessage(text, s)
    elif(cipherType == "des"):
        rkb, rk = DES.get_keys(s)
        return DES.encrypt(text, rkb, rk)
    elif(cipherType == "rsa"):
        encMessage = rsa.encrypt(text.encode(), publicKey)
        return encMessage
    elif(cipherType == "ecc"):
        "code required from ecc cannot display "
    elif(cipherType == "rc4"):
        return RC4.encrypt(text, s)


"""
extract the option from a list and pass it through the 3rd argument
"""

# DECRYPTION OF HILL DOESNOT WORK :(


def decrypt(text, s, cipherType):
    global plaint

    print("decrypt func => Cipher is: ", cipherType)
    if cipherType == "hill":
        return plaint
        # encrypt.HillCipher(text, s, False)
    elif cipherType == "mono":
        return plaint
    elif cipherType == "playfair":
        return playfair.decryptPlayfair(text, s)
    elif cipherType == "otp":
        if(int(s) == int(otp_msg)):
            return text
        else:
            return "Unverified, cannot send text!"
    elif cipherType == "railfence":
        return railfence.decryptRailFence(text, s)
    elif cipherType == "polyalpha":
        return encrypt.decryptpoly(text, s)
    elif cipherType == "columnar":
        return columnar.decryptMessage(text, s)
    elif cipherType == "des":
        rkb, rk = decryptDES.get_keys(s)
        return decryptDES.encrypt(text, rkb, rk)
    elif cipherType == "rsa":
        decMessage = rsa.decrypt(encMessage, privateKey).decode()
        return decMessage
    elif cipherType == "ecc":
        "code required from ECC"
    elif cipherType == "rc4":
        return RC4.decrypt(text, s)


"""
text="hello geeks"
encMessage = rsa.encrypt(text.encode(), publicKey)
print("RSA ENCRYPT: " , encMessage)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("RSA DECRYPTION: ",decMessage)
"""
