import hashlib
import random
import string

LEVELS = {
    "easy":   (6,  string.digits),
    "medium": (8,  string.ascii_lowercase + string.digits),
    "hard":   (12, string.ascii_letters + string.digits + "!@#$%^&*"),
}

def random_password(length, charset):
    return ''.join(random.choices(charset, k=length))

def generate_hash_file(level, count=10, filename="hashes.txt"):
    length, charset = LEVELS[level]
    passwords = []
    with open(filename, "w") as f:
        for _ in range(count):
            pw = random_password(length, charset)
            h = hashlib.md5(pw.encode()).hexdigest()
            f.write(h + "\n")
            passwords.append((pw, h))
    
    print(f"\nGenerated {count} {level} passwords:")
    print(f"{'Password':<20} {'MD5 Hash'}")
    print("-" * 55)
    for pw, h in passwords:
        print(f"{pw:<20} {h}")
    print(f"\nHashes saved to {filename}")

generate_hash_file("easy")