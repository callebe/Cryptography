import matplotlib.pyplot as plt
import numpy as np
from src import caesarCipher as caesar

ASCII_SIZE = 255

sampleA = "Luciano tem oito anos e possui uma família que admira muito. Ele gosta de desenhar seus familiares quando está de férias. Sua mãe chama-se Olívia e tem cabelos castanhos e longos. Ela gosta de assistir novelas e cultivar um jardim de rosas brancas. Douglas é o nome do pai de Luciano, que mora em outra casa. Eles se veem uma vez por semana e se divertem bastante quando estão juntos. O garoto possui ainda duas irmãs: Alice e Aline. As garotas são gêmeas e têm cinco anos. Elas gostam de brincar de bonecas e de jogar bola. O avô paterno de Luciano tem 86 anos e chama-se Heitor. A avó paterna tem 85 anos e gosta de jogar xadrez com os netos. Ela se chama Maria. Rita e Olavo são os nomes dos avós maternos de Luciano. Eles têm 74 e 76 anos e moram em uma cidade no interior do estado de São Paulo. Como o garoto mora no Rio de Janeiro, é preciso fazer uma viagem para visitar esses avós. Os tios por parte do pai de Luciano chamam-se Ricardo e Antônia. Já por parte de mãe, o garoto não possui tios. Ricardo é pai de Lucas e Gabriel, que são primos de Luciano. Sua tia Antônia está grávida de um garoto que se chamará Leonardo e será o primo mais novo de Luciano."

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


def frequencyAnalizer_Cracker( cipherText, plot = False ):

    freqSpecCipherText = frequencyAnalizer(cipherText, plot, 'Cipher Text')
    freqSpecSample     = frequencyAnalizer(sampleA, plot, 'Portuguese Sample')
    plt.show()

    # Searching for the most frequent Char on CipherText
    maxFreq       = 0
    maxFreqCharCT = 0

    for i in range(len(freqSpecCipherText)) :
        if freqSpecCipherText[i] > maxFreq :
            maxFreq       = freqSpecCipherText[i]
            maxFreqCharCT = i

    # Searching for the most frequent Char on the Sample
    maxFreq      = 0
    maxFreqCharS = 0
    for i in range(len(freqSpecSample)) :
        if freqSpecSample[i] > maxFreq :
            maxFreq     = freqSpecSample[i]
            maxFreqCharS = i

    #Key calculation
    return (maxFreqCharCT-maxFreqCharS)
    

def menu():

    print("Please, first provide the Cipher Text:")
    cipherText=input()
    print("----------------------------------")
    key = frequencyAnalizer_Cracker( cipherText, True )
    plainText=caesar.decrypt( key, cipherText )
    print("----------------------------------")
    print("The Key for encrypt mensage is:")
    print(key)
    print("The mensage is:")
    print(plainText)
        
    
if __name__ == "__main__":
    menu()