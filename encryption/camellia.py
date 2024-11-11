from Crypto.Cipher import Camellia
from Crypto.Random import get_random_bytes

def encrypt_text(key, plaintext):
    cipher = Camellia.new(key, Camellia.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

def decrypt_text(key, ciphertext):
    nonce = ciphertext[:16]
    tag = ciphertext[16:32]
    ciphertext = ciphertext[32:]
    cipher = Camellia.new(key, Camellia.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext
