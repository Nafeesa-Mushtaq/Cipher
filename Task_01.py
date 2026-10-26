import hashlib
import hmac

with open("data.txt", "w") as file:
    file.write("Transfer $100 to Alice")
SECRET_KEY = b"Integrity_Check_2024"

# Function to compute SHA-256 hash and HMAC of a file
def check_integrity(filepath):
    sha256_hash = hashlib.sha256()
    hmac_signature = hmac.new(SECRET_KEY, digestmod=hashlib.sha256)

    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break

            sha256_hash.update(chunk)
            hmac_signature.update(chunk)
    return sha256_hash.hexdigest(), hmac_signature.hexdigest()


initial_hash, initial_hmac = check_integrity("data.txt")

print("------ INITIAL INTEGRITY CHECK ------")
print("Initial Hash:", initial_hash)
print("Initial HMAC:", initial_hmac)

# Simulate an attack by modifying the file
with open("data.txt", "a") as file:
    file.write("Hacked!")

new_hash, new_hmac = check_integrity("data.txt")

print("\n------ AFTER SIMULATED ATTACK ------")
print("New Hash:", new_hash)
print("New HMAC:", new_hmac)

if (initial_hash != new_hash) or (not hmac.compare_digest(initial_hmac, new_hmac)):
    print("\nWARNING: INTEGRITY COMPROMISED")
else:
    print("\nFile integrity verified. No changes detected.")
