# (!) NOT TO BE SHOWN TO PARTICIPANTS (!)
#
# Example script to demonstrate how the
# solution to this challenge is found.
#
# (!) NOT TO BE SHOWN TO PARTICIPANTS (!)

plaintext: str = "pecan{5tr34mC1ph3r}"
ciphertext: list[int] = []

def encrpyt_demo() -> None:
    for i, c in enumerate(plaintext):
        ciphertext.append(ord(c) + i)
    print("Calculated ciphertext:", ciphertext)

def decrypt_demo() -> None:
    plaintext_chars: str = ""
    for i, c in enumerate(ciphertext):
        plaintext_chars += chr(c - i)
    print("Calculated plaintext:", plaintext_chars)

encrpyt_demo()
decrypt_demo()
