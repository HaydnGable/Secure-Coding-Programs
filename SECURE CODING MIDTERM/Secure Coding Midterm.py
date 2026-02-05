#hashlib for generating SHA-256 hashes, os for generating the nonce, and AESGCM for encryption and decryption
import hashlib
from os import urandom
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

#Get the user message encoded to utf-8
message = input("Enter a string: ").encode(encoding="utf-8")

#Generate hash of user input, store it, then print it
message_hash = hashlib.sha256(message).hexdigest()
print("Hash of original message:", message_hash)

#AES Key
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

#Generate a number to be used for the encryption and decryption, encrypt the text and print it
nonce = urandom(12)
encrypted_text = aesgcm.encrypt(nonce, message, None)
print("Encrypted text:", encrypted_text.hex())

#Decrypt the encrypted text using the nonce, then print it
decrypted_text = aesgcm.decrypt(nonce, encrypted_text, None)
print("Decrypted text:", decrypted_text)

#Generate hash of decrypted text, print it, then compare it to the previous hash
decrypted_hash = hashlib.sha256(decrypted_text).hexdigest()
print("Hash of message after decryption", decrypted_hash)

if message_hash == decrypted_hash:
    print("Hashes are the same, message is safe")
else:
    print("Hashes are not the same, message is NOT safe")
