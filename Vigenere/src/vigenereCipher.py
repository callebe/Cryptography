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

def menu():
    stop = True
    while stop:
        print("Do you wanna Encrypt[1] or Decrypt[2] a mensage or Exit[0]?")
        selectedOption=input()
        if selectedOption == '1':
            print("Please, first provide the key:")
            key=input()
            print("The Plain Mesage:")
            plainText=input()
            cipherText=encrypt( key,  plainText )
            print("The Cipher mesage is:")
            print(cipherText)

        elif selectedOption == '2':
            print("Please, first provide the key:")
            key=input()
            print("The Chiper Mesage:")
            chiperText=input()
            plainText=decrypt( key, chiperText )
            print("The plainText mensage is:")
            print(plainText)

        else:
            stop = False
        
    
if __name__ == "__main__":
    menu()
