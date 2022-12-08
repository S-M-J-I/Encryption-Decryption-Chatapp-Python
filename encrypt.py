def encrypt(text,s):
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
 

def polyalphabetic(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

# Python3 code to implement Hill Cipher
 
keyMatrix = [[0] * 3 for i in range(3)]
 
# Generate vector for the message
messageVector = [[0] for i in range(3)]
 
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]
 
# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
# Following function encrypts the message
def encrypthill(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):
 
    # Get key matrix from the key string
    getKeyMatrix(key)
 
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    encrypthill(messageVector)
 
    # Generate the encrypted text
    # from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
 
    return CipherText
    # Finally print the ciphertext
    #print("Ciphertext: ", "".join(CipherText))
 
