# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def load_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def save_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

def decrypt_aes_ecb(cypher_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypt_data = unpad(cipher.decrypt(cypher_data), AES.block_size)
    return decrypt_data

def decrypt_aes_cbc(cypher_data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    decrypt_data = unpad(cipher.decrypt(cypher_data), AES.block_size)
    return decrypt_data