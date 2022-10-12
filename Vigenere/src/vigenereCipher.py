ASCII_SIZE = 256

def encrypt( key,  plainText ):
    cipherText = ""
    keyLength = len(key)
    keyIdex = 0
    for letter in plainText:
        cipherText = cipherText + chr((ord(letter)+ord(key[keyIdex]))%ASCII_SIZE)
        keyIdex = (keyIdex + 1) % keyLength
    return cipherText

def decrypt( key, cipherText ):
    plainText = ""
    keyLength = len(key)
    keyIdex = 0
    for letter in cipherText:
        plainText = plainText + chr((ord(letter)-ord(key[keyIdex]))%ASCII_SIZE)
        keyIdex = (keyIdex + 1) % keyLength
    return plainText