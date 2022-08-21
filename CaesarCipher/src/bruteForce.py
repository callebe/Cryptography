from src import languageDetector as langDet
from src import caesarCipher as cipher

ASCII_SIZE = 256
WORD_LIST_FILE = 'data/mostFrewPortugueseWords.txt'
langThreshold = 30

def bruteForce( cipherText ):
    stop            = True
    key             = -1
    keyCandidate    = 0
    while stop:
        plainText = ""
        for letter in cipherText:
            plainText = plainText + chr((ord(letter)-keyCandidate)%ASCII_SIZE)
        langDet.loadWordFile(WORD_LIST_FILE)
        combinationCounter, foundedWords, matchPorcentage = langDet.checkMatches( plainText )
        # print(plainText)
        # print("This mensage makes sense?[y, n]")
        # selectedOption=input()
        if combinationCounter>0 and matchPorcentage > langThreshold:
            stop = False
            key = keyCandidate
            print(foundedWords)
            print(' -- '+str(matchPorcentage))
            print(' ++ '+str(combinationCounter))
        else:
            keyCandidate = keyCandidate + 1

    return key

def menu():

    print("Please, first provide the Cipher Text:")
    cipherText=input()
    print(len(cipherText))
    print("----------------------------------")
    key=bruteForce(cipherText)
    print("----------------------------------")
    print("The Key for encrypt mensage is:")
    print(key)
    print("The mensage is:")
    print(cipher.decrypt(key,cipherText))
    print(len(cipherText))
    
        
    
if __name__ == "__main__":
    menu()