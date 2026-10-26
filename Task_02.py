import random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# TASK 01: VICTIM'S ENCRYPTION
message = b"TopSecret"
random_key = random.randint(0, 255)

# Create an 8-byte DES key
key = b'\x00' * 7 + bytes([random_key])

# Encrypt the message using DES in ECB mode
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, DES.block_size))

print("------ VICTIM'S ENCRYPTION ------")
print("Original Message :", message.decode())
print("Random Key       :", random_key)
print("DES Key (Hex)    :", key.hex().upper())
print("Ciphertext (Hex) :", ciphertext.hex().upper())


# TASK 02: ATTACKER'S BRUTE-FORCE
def brute_force_des(ciphertext):
    print("\n------ ATTACKER'S BRUTE-FORCE ------")

    for integer in range(256):
        
        # Construct the candidate DES key
        candidate_key = b'\x00' * 7 + bytes([integer])

        # Attempt decryption using the candidate key
        try:
            cipher = DES.new(candidate_key, DES.MODE_ECB)
            decrypted = unpad(
                cipher.decrypt(ciphertext),
                DES.block_size
            )

            # Check whether the decrypted text is readable
            decoded_message = decrypted.decode("utf-8")

            if decoded_message.isprintable():
                print(f"[SUCCESS] Key found: {integer}")
                print("Decrypted Message:", decoded_message)
                return

        except (ValueError, UnicodeDecodeError):
            continue

    print("[FAILED] Correct key not found.")

# Executing the brute-force attack
brute_force_des(ciphertext)