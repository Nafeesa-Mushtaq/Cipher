
import argparse
import os
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


KEY_FILE = "key.bin"
ENCRYPTED_FILE = "encrypted.bin"
DECRYPTED_FILE = "decrypted.txt"


def encrypt_file(filepath):
    filepath = Path(filepath)

    if not filepath.is_file():
        raise FileNotFoundError(f"File not found: {filepath}")

    data = filepath.read_bytes()

    key = os.urandom(32)  # 256-bit AES key
    iv = os.urandom(16)   # 128-bit initialization vector

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    Path(KEY_FILE).write_bytes(key + iv)
    Path(ENCRYPTED_FILE).write_bytes(ciphertext)

    print("Encryption successful.")
    print("Key and IV saved to:", KEY_FILE)
    print("Ciphertext saved to:", ENCRYPTED_FILE)


def decrypt_file():
    key_data = Path(KEY_FILE).read_bytes()

    if len(key_data) != 48:
        raise ValueError("Invalid key file.")

    key = key_data[:32]
    iv = key_data[32:48]

    ciphertext = Path(ENCRYPTED_FILE).read_bytes()

    if not ciphertext or len(ciphertext) % AES.block_size != 0:
        raise ValueError("Invalid ciphertext.")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    )

    Path(DECRYPTED_FILE).write_bytes(plaintext)

    print("Decryption successful.")
    print("Decrypted file saved to:", DECRYPTED_FILE)


def main():
    parser = argparse.ArgumentParser(
        description="AES-256-CBC file encryption and decryption"
    )

    parser.add_argument(
        "action",
        choices=["encrypt", "decrypt"]
    )

    parser.add_argument(
        "filepath",
        nargs="?"
    )

    args = parser.parse_args()

    try:
        if args.action == "encrypt":
            if not args.filepath:
                parser.error("Provide a file path for encryption.")
            encrypt_file(args.filepath)
        else:
            decrypt_file()

    except (OSError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
