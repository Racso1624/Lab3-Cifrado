from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import io

def read_key_from_file(key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    return key

def decrypt_image_ecb(encrypted_data, key):
    # Create AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the image data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Unpad the decrypted data
    unpadded_data = unpad(decrypted_data, AES.block_size)

    # Convert byte data to PIL Image
    image = Image.open(io.BytesIO(unpadded_data))

    return image

if __name__ == "__main__":
    key_file = './data/mr-increible.key'  # Ruta al archivo de la llave
    key = bytes.fromhex('406845db899854cc23484d6f3f28f3f7')

    # Leer la imagen cifrada
    with open('./data/mr-increible_encrypted_image.jpeg', 'rb') as file:
        encrypted_data = file.read()

    # Descifrar la imagen
    decrypted_image = decrypt_image_ecb(encrypted_data, key)

    # Mostrar la imagen descifrada
    decrypted_image.show()