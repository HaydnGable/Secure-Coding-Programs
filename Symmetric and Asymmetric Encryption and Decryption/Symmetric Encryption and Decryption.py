word = 'tacos'
key = 4
encrypted_word = ''
decrypted_word = ''

for i in word:
    i = ord(i)
    i = i + key
    i = chr(i)
    encrypted_word = encrypted_word + i
print(encrypted_word)

for i in encrypted_word:
    i = ord(i)
    i = i - key
    i = chr(i)
    decrypted_word = decrypted_word + i
print(decrypted_word)
