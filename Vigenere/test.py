
from msilib.schema import Class
import sys

from src import vigenereCipher as vigenere
from src import kasiskiAlgo as kasiski

def test_getLongestSubStr( ):
    # Arrange
    cipherText = "abfcda asdefabfcdagvcasd asdc xfdqasdasd as "

    # Act
    return_subStrList = kasiski.getLongestSubStr( cipherText )

    # Assert
    print(12)

def menuKeyCal():
    # plainText = "As frutas vermelhas que cairam devem ser jogadas fora"
    # sampleA = "Luciano tem oito anos e possui uma família que admira muito. Ele gosta de desenhar seus familiares quando está de férias. Sua mãe chama-se Olívia e tem cabelos castanhos e longos. Ela gosta de assistir novelas e cultivar um jardim de rosas brancas. Douglas é o nome do pai de Luciano, que mora em outra casa. Eles se veem uma vez por semana e se divertem bastante quando estão juntos. O garoto possui ainda duas irmãs: Alice e Aline. As garotas são gêmeas e têm cinco anos. Elas gostam de brincar de bonecas e de jogar bola. O avô paterno de Luciano tem 86 anos e chama-se Heitor. A avó paterna tem 85 anos e gosta de jogar xadrez com os netos. Ela se chama Maria. Rita e Olavo são os nomes dos avós maternos de Luciano. Eles têm 74 e 76 anos e moram em uma cidade no interior do estado de São Paulo. Como o garoto mora no Rio de Janeiro, é preciso fazer uma viagem para visitar esses avós. Os tios por parte do pai de Luciano chamam-se Ricardo e Antônia. Já por parte de mãe, o garoto não possui tios. Ricardo é pai de Lucas e Gabriel, que são primos de Luciano. Sua tia Antônia está grávida de um garoto que se chamará Leonardo e será o primo mais novo de Luciano."
    sampleA = "abablcklmcvbfgcqwqqdrthbabablcklmcvbfgcqwqqdrthbabablcklmcvbfgcqwqqdrthbabablcklmcvbfgcqwqqdrthbabablcklmcvbfgcqwqqdrthb"
    key = "tes"
    cipherText = vigenere.encrypt( key,  sampleA )
    # expected_KeyLength = len(key)
    return_keyLength = kasiski.calcKeyLength(cipherText)
    print(return_keyLength)

def menuDecEnc():
    stop = True
    while stop:
        print("Do you wanna Encrypt[1] or Decrypt[2] a mensage or Exit[0]?")
        selectedOption=input()
        if selectedOption == '1':
            print("Please, first provide the key:")
            key=input()
            print("The Plain Mesage:")
            plainText=input()
            cipherText=vigenere.encrypt( key,  plainText )
            print("The Cipher mesage is:")
            print(cipherText)

        elif selectedOption == '2':
            print("Please, first provide the key:")
            key=input()
            print("The Chiper Mesage:")
            chiperText=input()
            plainText=vigenere.decrypt( key, chiperText )
            print("The plainText mensage is:")
            print(plainText)

        else:
            stop = False

if __name__ == "__main__":
    # menuDecEnc()
    #menuKeyCal()
    test_getLongestSubStr()