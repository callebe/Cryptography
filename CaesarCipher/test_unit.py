import sys
import pytest
import logging

from src import caesarCipher as caesar
from src import bruteForce   as bF

# LOGGER.info('Exemple')
# LOGGER.warning('Exemple')
# LOGGER.error('Exemple')
# LOGGER.critical('Exemple')

LOGGER = logging.getLogger(__name__)

def test_CaesarCipher_Encrypt () :

    # Arrange
    key = 3
    plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'
    expected_cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'

    # Act
    cipherText = caesar.encrypt( key,  plainText )

    # Assert
    assert expected_cipherText == cipherText , "CipherText from Encrypt using Caesar Cipher Matches"

def test_CaesarCipher_Decrypt () :

    # Arrange
    key = 3
    cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
    expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

    # Act
    plainText = caesar.decrypt( key,  cipherText )

    # Assert
    assert expected_plainText == plainText, "Plain text from Decrypt using Caesar Cipher Matches"
    
def test_bruteForce ():

    # Arrange
    cipherText = 'Dv#iuxwdv#yhuphokdv#txh#fdludp#ghyhp#vhu#mrjdgdv#irud'
    expected_key = 3
    expected_plainText = 'As frutas vermelhas que cairam devem ser jogadas fora'

    # Act
    key = bF.bruteForce(cipherText)
    plainText = caesar.decrypt( key, cipherText )

    # Assert
    assert expected_key       == key       , "The Caesar Cipher encrypt key using brute force stratege Matches"
    assert expected_plainText == plainText , "The decrypted Plain text using brute force stratege Matches"