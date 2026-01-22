def calculate_d(e, z):
    for d in range(1, z):
        if (e * d) % z == 1:
            return d
#word to be decrypted, word after encryption, and word after decryption
word = 'TACOS'
encrypted_word = []
decrypted_word = ''

#two prime numbers that aren't the same
p = 7
q = 13

n = p * q
z = (p - 1) * (q - 1)

#a coprime of z that is less than n
e = 5

d = calculate_d(e, z)

#keys used for encryption and decryption
public_key = (e, n)
private_key = (d, n)

#encrypt the word and store in encrypted_word empty list
for m in word:
    m = ord(m)
    m = (m ** e) % n
    encrypted_word.append(m)

#decrypt the encrypted word and store in decrypted_word empty string
for c in encrypted_word:
    c = (c ** d) % n
    c = chr(c)
    decrypted_word = decrypted_word + c

#dump all the data to make sure it works
print('Original message: ', word)
print('Encrypted message: ', encrypted_word)
print('Decrypted message: ', decrypted_word)
print('Public key: ',public_key)
print('Private key: ', private_key)

