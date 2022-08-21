from itertools import combinations


WORD_LIST_FILE = 'mostFrewPortugueseWords.txt'
wordList = []

def loadWordFile( fileName ):
    
    file = open(fileName, "r")

    for line in file.read().split('\n'):
        words = line.split(' ')
        wordList.append(words[0])
    
    file.close()
    return True

def checkMatches( plainText ):
    combinationCounter = 0
    foundedWords = []
    matchPorcentage = 0
    plainTextLength = len(plainText)
    for word in wordList:
        wordLength = len(word)
        if(plainTextLength > wordLength):
            finish = wordLength
            for begin in range(0,plainTextLength - wordLength):
                if plainText[begin:finish] == word:
                    combinationCounter = combinationCounter + 1
                    plainText = plainText[0:begin] + plainText[finish:]
                    foundedWords.append(word)
                    matchPorcentage = matchPorcentage + wordLength
                finish = finish + 1
    
    matchPorcentage = (matchPorcentage * 100) / plainTextLength

    return combinationCounter, foundedWords, matchPorcentage


if __name__ == "__main__":
    # menu()
    plainText = 'Olá pessoal'
    loadWordFile(WORD_LIST_FILE)
    combinationCounter, foundedWords, matchPorcentage = checkMatches( plainText )
    print('Z>>'+str(combinationCounter))
    print('P>>'+str(matchPorcentage))
