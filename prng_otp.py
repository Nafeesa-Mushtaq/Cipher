
import secrets


def generate_random_bits(length):
    return "".join(secrets.choice("01") for _ in range(length))


def xor_bits(message, key):
    return "".join(
        str(int(m) ^ int(k))
        for m, k in zip(message, key)
    )


message = generate_random_bits(128)
key = generate_random_bits(128)

ciphertext = xor_bits(message, key)
decrypted = xor_bits(ciphertext, key)

print("Original message:", message)
print("Random key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted)
print("Decryption successful:", decrypted == message)
