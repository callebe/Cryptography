ASCII_SIZE = 256

def bruteForce( cipherText ):
    stop            = True
    key             = -1
    keyCandidate    = 0
    while stop:
        plainText = ""
        for letter in cipherText:
            plainText = plainText + chr((ord(letter)-keyCandidate)%ASCII_SIZE)
        print(plainText)
        print("This mensage makes sense?[y, n]")
        selectedOption=input()
        if selectedOption == 'y':
            stop = False
            key = keyCandidate
        else:
            keyCandidate = keyCandidate + 1

    return key

def menu():

    print("Please, first provide the Cipher Text:")
    cipherText=input()
    print("----------------------------------")
    key=bruteForce(cipherText)
    print("----------------------------------")
    print("The Key for encrypt mensage is:")
    print(key)
        
    
if __name__ == "__main__":
    menu()