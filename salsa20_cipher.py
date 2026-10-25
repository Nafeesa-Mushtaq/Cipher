
from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes


message = b"Hello, this is a Salsa20 encryption demo!"

key = get_random_bytes(32)
cipher = Salsa20.new(key=key)

nonce = cipher.nonce
ciphertext = cipher.encrypt(message)

print("Original message:", message.decode())
print("Key:", key.hex())
print("Nonce:", nonce.hex())
print("Ciphertext:", ciphertext.hex())

decrypt_cipher = Salsa20.new(key=key, nonce=nonce)
decrypted = decrypt_cipher.decrypt(ciphertext)

print("Decrypted message:", decrypted.decode())
print("Decryption successful:", decrypted == message)
