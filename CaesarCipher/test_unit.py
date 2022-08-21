from msilib.schema import Class
import sys
import pytest
import logging

from src import caesarCipher as caesar
from src import bruteForce as bF
from src import frequencyAnalizer as fA

# LOGGER.info('Exemple')
# LOGGER.warning('Exemple')
# LOGGER.error('Exemple')
# LOGGER.critical('Exemple')

LOGGER = logging.getLogger(__name__)



@pytest.mark.parametrize(
    "plainText, key, cipherText",
    [
        ("As frutas vermelhas que cairam devem ser jogadas fora",3,"Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud"),
        ("O amor mora no coração daqueles que crêem", 8, "W(iuwz(uwzi(vw(kwziïëw(liy}mtm{(y}m(kzòmu"),
    ],
)
class TestGroup_CaesarCipher:
    """A class with common parameters, plainText, key, cipherText."""

    # @pytest.fixture
    # def fixt(self):
    #     """This fixture will only be available within the scope of TestGroup"""
    #     return 123

    def test_Encrypt (self, plainText , key , cipherText) :

        # Arrange
        # key = 3
        # plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'
        # expected_cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'

        # Act
        return_cipherText = caesar.encrypt( key,  plainText )

        # Assert
        assert cipherText == return_cipherText , "CipherText from Encrypt using Caesar Cipher Matches"

    def test_Decrypt (self, plainText , key,  cipherText) :

        # Arrange
        # key = 3
        # cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
        # expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

        # Act
        return_plainText = caesar.decrypt( key,  cipherText )

        # Assert
        assert plainText == return_plainText, "Plain text from Decrypt using Caesar Cipher Matches"
        
    def test_crackBruteForce (self, plainText, key,  cipherText ):

        # Arrange
        # cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
        # expected_key = 3
        # expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

        # Act
        return_key = bF.bruteForce(cipherText)
        return_plainText = caesar.decrypt( return_key, cipherText )

        # Assert
        assert key       == return_key       , "The Caesar Cipher encrypt key using brute force stratege Matches"
        assert plainText == return_plainText , "The decrypted Plain text using brute force stratege Matches"

    def test_crackFrequenceAnalyzer(self, plainText, key,  cipherText ):

        # Arrange
        # cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
        # expected_key = 3
        # expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

        # Act
        return_key = fA.frequencyAnalizer_Cracker(cipherText)
        return_plainText = caesar.decrypt( return_key, cipherText )

        # Assert
        assert key       == return_key       , "The Caesar Cipher encrypt key using frequence analysis stratege Matches"
        assert plainText == return_plainText , "The decrypted Plain text using frequence analysis stratege Matches"