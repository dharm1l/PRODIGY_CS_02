key = 123

# Encrypt the image
with open("certs.jpg", 'rb') as file:
    image = bytearray(file.read())

# XOR each byte with the key for encryption
for index, value in enumerate(image):
    image[index] = value ^ key

# Save the encrypted image to a new file
with open("certs_encrypted.jpg", 'wb') as file:
    file.write(image)

# Now decrypt the image by applying XOR again with the same key
with open("certs_encrypted.jpg", 'rb') as file:
    encrypted_image = bytearray(file.read())

# XOR each byte with the key for decryption
for index, value in enumerate(encrypted_image):
    encrypted_image[index] = value ^ key

# Save the decrypted image to a new file
with open("certs_decrypted.jpg", 'wb') as file:
    file.write(encrypted_image)
