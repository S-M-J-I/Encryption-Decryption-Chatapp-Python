import numpy as np

def encryptceaser(text,s):
    print("TEXT: ", text)
    result = ""
  
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
# This function returns the
# encrypted text generated
# with the help of the key
def cipherpolyalphabetic(string, key):
    cipher_text = []
    key=generateKey(string, key)
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
def decryptpoly(cipher_text, key):
    print("cipher:",cipher_text)
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in cipher_text]
    plaintext = ""
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    print("plaiintext: ", plaintext)
    return plaintext
"""
    print("cipher= ",cipher_text)
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    print("decrypted " , orig_text)
    return("" . join(orig_text))
"""
def polyalphabetic(string, key, encrypt=True):
    """
    params:
        string: string => the string we want to encrypt/decrypt
        key: string => the string we use as the keyword
        encrypt: bool => True to make 'string' encrypt, False to decrypt 'string'
    """
    result = ''
    print("ENCRYPT:" + string)
    if key == '':
        return "No key"

    for i in range(len(string)):
        letter_n = ord(string[i])
        key_n = ord(key[i % len(key)])

        if encrypt == True:
            # encrypt
            value = (letter_n + key_n) % 26
        else:
            # decrypt
            value = (letter_n - key_n) % 26

        result += chr(value)
    print(result)

    return result

keys={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n'}

def encryptmono(text):
    text=str(text)
    encrypting=[]
    for l in text:
        encrypting.append(keys.get(l,l))
    print(''.join(encrypting))
    return ''.join(encrypting)
def deciphermono(text):
    reverse_keys={}
    for key,value in keys.items():
         reverse_keys[value]=key
    text=str(text)
    decrypted=[]
    for l in text:
        decrypted.append(reverse_keys.get(l,l))
    print(''.join(decrypted))
    return ''.join(decrypted)