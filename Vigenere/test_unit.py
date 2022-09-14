from msilib.schema import Class
import sys
import pytest
import logging

from src import vigenereCipher as vigenere
from src import kasiskiAlgo as kasiski
# from src import bruteForce as bF
# from src import frequencyAnalizer as fA

# LOGGER.info('Exemple')
# LOGGER.warning('Exemple')
# LOGGER.error('Exemple')
# LOGGER.critical('Exemple')

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "plainText, key",
    [
        ("As frutas vermelhas que cairam devem ser jogadas fora","test"),
        ("O amor mora no coração daqueles que crêem","boralaamigo"),
        ("Não existe amor em SP", "nerobolo")
    ],
)
class TestGroup_vigenereCipher:
    """A class with common parameters, plainText, key, cipherText."""

    # @pytest.fixture
    # def fixt(self):
    #     """This fixture will only be available within the scope of TestGroup"""
    #     return 123

    def test_EncryptDecryptSeq(self, plainText , key):
        # Arrange

        # Act
        return_cipherText = vigenere.encrypt( key,  plainText )
        return_plainText = vigenere.decrypt( key,  return_cipherText )

        # Assert
        assert plainText == return_plainText , "PlainText from Encrypt/Decrypt using Caesar Cipher Matches"

    # def test_crackBruteForce (self, plainText, key,  cipherText ):

    #     # Arrange
    #     # cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
    #     # expected_key = 3
    #     # expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

    #     # Act
    #     return_key = bF.bruteForce(cipherText)
    #     return_plainText = caesar.decrypt( return_key, cipherText )

    #     # Assert
    #     assert key       == return_key       , "The Caesar Cipher encrypt key using brute force stratege Matches"
    #     assert plainText == return_plainText , "The decrypted Plain text using brute force stratege Matches"

    # def test_crackFrequenceAnalyzer(self, plainText, key,  cipherText ):

    #     # Arrange
    #     # cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
    #     # expected_key = 3
    #     # expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

    #     # Act
    #     return_key = fA.frequencyAnalizer_Cracker(cipherText)
    #     return_plainText = caesar.decrypt( return_key, cipherText )

    #     # Assert
    #     assert key       == return_key       , "The Caesar Cipher encrypt key using frequence analysis stratege Matches"
    #     assert plainText == return_plainText , "The decrypted Plain text using frequence analysis stratege Matches"

class TestGroup_kasiskiAlgo:

    def test_getLongestSubStr( self ):
        # Arrange
        cipherText = "abfcda asdefabfcdagvcasd asdc xfdqasdasd as "
        expected_strList = kasiski.subStrOccurrenceList()
        strOcc1 = kasiski.subStrOccurrence(
                    "abfcda",
                    20
                )
        strOcc2 = kasiski.subStrOccurrence(
                    "asd as",
                    0
                )
        expected_strList.append(strOcc1)
        expected_strList.append(strOcc2)

        # Act
        return_subStrList = kasiski.getLongestSubStr( cipherText )

        # Assert
        assert return_subStrList.length == 2 , "The number of substrings founded on the CipherText"
        assert return_subStrList.subStrList[0].subStr == expected_strList.subStrList[0].subStr , "Return the longest Substrings founded on the CipherText, element 1"
        assert return_subStrList.subStrList[1].subStr == expected_strList.subStrList[1].subStr , "Return the longest Substrings founded on the CipherText, element 2"
    
    def test_calcPossibleKeys( self ):
        # Arrange
        cipherText = "abfcda asdefabfcdagvcasd asdc xfdqasdasd as "
        expected_keyLengths = [12, 16]

        # Act
        return_keys = kasiski.calcPossiblePatternDistance( cipherText )

        # Assert
        assert return_keys == expected_keyLengths, "The Expected possible keys matches with the expected key array"

    def test_calcDivisors( self ):
        # Arrange
        keyLengths = [ 5, 25, 10, 20, 35 ]
        expected_divisors = [
            [5, 1],
            [25, 5, 1],
            [10, 5, 2, 1],
            [20, 10, 5, 4, 2, 1],
            [35, 7, 5, 1]
        ]

        # Act
        return_divisors = kasiski.calcDivisors( keyLengths )

        # Assert
        assert return_divisors == expected_divisors, "The Expected Divisors Matches with the return"

    def test_calcGCD( self ):
        # Arrange
        keys = [ 5, 25, 10, 20, 35 ]
        expected_GCD = 5

        # Act
        return_GCD = kasiski.calcGCD( keys )

        # Assert
        assert return_GCD == expected_GCD, "The expected GCD Matches with the return"

    def test_calcKeyLength( self ):
        # Arrange
        plainText = "As frutas vermelhas que cairam devem ser jogadas fora"
        key = "test"
        cipherText = vigenere.encrypt( key,  plainText )
        expected_KeyLength = len(key)

        # Act
        return_keyLength = kasiski.calcKeyLength(cipherText)

        # Assert
        assert return_keyLength == expected_KeyLength, "The expected GCD Matches with the return"