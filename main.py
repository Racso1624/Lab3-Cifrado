from functions import *
import hashlib

# Parte 1

key_1 = load_file('./data/mr-increible.key')
key_1 = key_1.decode('utf-8')
image_1 = load_file('./data/mr-increible_encrypted_image.jpeg')
decrypted_image_1 = decrypt_aes_ecb(image_1, bytes.fromhex(key_1))
save_file('./results/mr-increible-decrypted.jpeg', decrypted_image_1)

key_2 = load_file('./data/ayno.key')
key_2 = key_2.decode('utf-8')
image_2 = load_file('./data/ayno_encrypted_image.jpeg')
decrypted_image_2 = decrypt_aes_cbc(image_2, bytes.fromhex(key_2))
save_file('./results/ayno-decrypted.jpeg', decrypted_image_2)