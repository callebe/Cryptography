import matplotlib.pyplot as plt

MIN_SUBSTRING_LEN = 3

ASCII_SIZE = 255

sampleA = "Luciano tem oito anos e possui uma família que admira muito. Ele gosta de desenhar seus familiares quando está de férias. Sua mãe chama-se Olívia e tem cabelos castanhos e longos. Ela gosta de assistir novelas e cultivar um jardim de rosas brancas. Douglas é o nome do pai de Luciano, que mora em outra casa. Eles se veem uma vez por semana e se divertem bastante quando estão juntos. O garoto possui ainda duas irmãs: Alice e Aline. As garotas são gêmeas e têm cinco anos. Elas gostam de brincar de bonecas e de jogar bola. O avô paterno de Luciano tem 86 anos e chama-se Heitor. A avó paterna tem 85 anos e gosta de jogar xadrez com os netos. Ela se chama Maria. Rita e Olavo são os nomes dos avós maternos de Luciano. Eles têm 74 e 76 anos e moram em uma cidade no interior do estado de São Paulo. Como o garoto mora no Rio de Janeiro, é preciso fazer uma viagem para visitar esses avós. Os tios por parte do pai de Luciano chamam-se Ricardo e Antônia. Já por parte de mãe, o garoto não possui tios. Ricardo é pai de Lucas e Gabriel, que são primos de Luciano. Sua tia Antônia está grávida de um garoto que se chamará Leonardo e será o primo mais novo de Luciano."

class subStrOccurrence:
    def __init__( self, subStr, postision ):
        self.subStr = subStr
        self.occurrence = 1
        self.postisions = [postision]

class subStrOccurrenceList:
    def __init__( self ):
        self.subStrList = []
        self.length = 0

    def append(self, subStrOccu ):
        
        occurencePosition = -1
        for i in range(self.length):
            if(self.subStrList[i].subStr == subStrOccu.subStr):
                occurenceExist = True
                occurencePosition = i

        if(occurencePosition < 0):
            self.subStrList.append(subStrOccu)
            self.length = self.length +1
        
        else:
            self.subStrList[i].postisions = self.subStrList[i].postisions + subStrOccu.postisions
            self.subStrList[i].occurrence = self.subStrList[i].occurrence + 1



def plotSpectrum(X,Y, Title):

    plt.figure(Title)
    plt.bar(X, Y)

def frequencyAnalizer( input, Title, plot ):

    frequencySpectrumY = [0] * ASCII_SIZE
    frequencySpectrumX =  [ i for i in range(ASCII_SIZE) ]
    for letter in input:
        frequencySpectrumY[ord(letter)] = frequencySpectrumY[ord(letter)] + 1
    if plot == True:
        plotSpectrum(frequencySpectrumX,frequencySpectrumY, Title)

    return frequencySpectrumY

def searchRepeatedSubStrings( input, subStrMaxLen ):

    subStr = subStrOccurrenceList()

    for subStart in range(len(input)-subStrMaxLen):
        
        # Get the reference substring
        refSubString = input[subStart : subStart + subStrMaxLen]
        
        # Seaching for repeated substring pattern
        position = subStart + subStrMaxLen
        for i in range(len(input)-subStrMaxLen):
            if(position==len(input)):
                position = 0
            if(refSubString == input[position : position + subStrMaxLen]):
                subStr.append(
                    subStrOccurrence(
                        refSubString,
                        position
                    )
                )
            position = position + 1

    return subStr

def getLongestSubStr( text ):
    
    for substrlen in range(int(len(text)/2), MIN_SUBSTRING_LEN, -1):
        subStrList = searchRepeatedSubStrings( text, substrlen )
        if(subStrList.length > 0 ):
            break

    return subStrList

def calcPossibleKeys( text ):
    strList = getLongestSubStr( text )


def menu():

    str="olam pessoal olam ra amada amaico"
    output = []
    print(int(len(str)/2))
    

    print("AAA")
    
if __name__ == "__main__":
    menu()

