This program takes a message from the user, makes a hash of the message, encrypts it, decrypts it, then makes another hash of the decrypted text and compares it against the original hash to verify it's integrity.

This solution upholds confidentiality by encrypting the message using AES so that only someone with the key would be able to decrypt the message.
This solution upholds integrity by generating a hash before and after encryption so that the recipient can verify the message was not changed before receiving it.
This solution does not focus on availability. 

This solution uses entropy through generating a nonce to be used for encryption and decryption alongside the key. The nonce is a random number used to increase the security of the encryption and decryption process.

The key used for encryption and decryption is generated using AESGCM with a bit length of 256.