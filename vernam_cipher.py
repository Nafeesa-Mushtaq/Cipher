
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

if not key:
    print("Key cannot be empty.")
else:
    ciphertext = ""

    for i, char in enumerate(plaintext):
        ciphertext += chr(ord(char) ^ ord(key[i % len(key)]))

    print("Ciphertext:", repr(ciphertext))

    decrypted = ""

    for i, char in enumerate(ciphertext):
        decrypted += chr(ord(char) ^ ord(key[i % len(key)]))

    print("Decrypted plaintext:", decrypted)
