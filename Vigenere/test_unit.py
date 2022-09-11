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
