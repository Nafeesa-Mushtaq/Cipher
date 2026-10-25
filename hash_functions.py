
import hashlib
import hmac
from pathlib import Path


def calculate_hash(text, algorithm):
    data = text.encode("utf-8")
    return hashlib.new(algorithm, data).hexdigest()


def get_file_hash(filepath, algorithm="sha256"):
    hasher = hashlib.new(algorithm)

    # Read in chunks to support large files.
    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()


def hmac_demo():
    message = b"Hello, this is a secure message"
    secret_key = b"my_secret_key"

    signature = hmac.new(
        secret_key, message, hashlib.sha256
    ).hexdigest()

    print("\n--- HMAC-SHA256 ---")
    print("Original message:", message.decode())
    print("HMAC signature:", signature)

    verification = hmac.new(
        secret_key, message, hashlib.sha256
    ).hexdigest()

    print(
        "Original message verified:",
        hmac.compare_digest(signature, verification)
    )

    tampered_message = b"Hello, this is a changed message"
    tampered_signature = hmac.new(
        secret_key, tampered_message, hashlib.sha256
    ).hexdigest()

    print(
        "Tampered message verified:",
        hmac.compare_digest(signature, tampered_signature)
    )


def file_integrity_demo():
    filepath = Path("data.txt")
    filepath.write_text(
        "This is the original file content.",
        encoding="utf-8"
    )

    original_hash = get_file_hash(filepath)

    print("\n--- File Integrity Checker ---")
    print("Original SHA-256:", original_hash)

    content = filepath.read_text(encoding="utf-8")
    modified_content = content.replace("original", "modified", 1)
    filepath.write_text(modified_content, encoding="utf-8")

    modified_hash = get_file_hash(filepath)

    print("Modified SHA-256:", modified_hash)
    print("Hash changed:", original_hash != modified_hash)


def main():
    text = "Hello, Cryptography Lab!"

    print("--- Hash Functions ---")
    for algorithm in ("md5", "sha1", "sha256", "sha512"):
        digest = calculate_hash(text, algorithm)
        print(f"{algorithm.upper()}: {digest}")
        print(f"Output length: {len(digest)} hexadecimal characters\n")

    hmac_demo()
    file_integrity_demo()


if __name__ == "__main__":
    main()
