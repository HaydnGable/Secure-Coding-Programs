import hashlib

input_string = "I like tacos."

hash_object = hashlib.sha256(input_string.encode('utf-8'))

hex_digest = hash_object.hexdigest()

print("Original string: " + input_string)
print("SHA256 hash: " + hex_digest)
