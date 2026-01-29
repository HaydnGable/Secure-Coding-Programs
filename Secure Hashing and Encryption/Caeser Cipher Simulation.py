word = input("Enter a word to be encrypted: ")
key = int(input("Enter a value between 1 and 10 to be added for encryption: "))

while key > 10 or key < 1:
    if key > 10:
        print("That number was too high.")
    elif key < 1:
        print("That number was too low.")
    key = int(input("Enter a value between 1 and 10 to be added for encryption: "))

encrypted_word = ''
decrypted_word = ''

for i in word:
    i = ord(i)
    i = i + key
    i = chr(i)
    encrypted_word = encrypted_word + i

for i in encrypted_word:
    i = ord(i)
    i = i - key
    i = chr(i)
    decrypted_word = decrypted_word + i

print("Encrypted text: " + encrypted_word)
print("Decrypted text: " + decrypted_word)
