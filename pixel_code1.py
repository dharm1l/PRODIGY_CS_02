from PIL import Image

def encrypt_image_xor(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # XOR each color channel with the key
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    
    image.save(output_path)
    print("Encryption complete.")

def decrypt_image_xor(input_path, output_path, key):
    # Decryption is the same as encryption since XOR is reversible
    image = Image.open(input_path)
    pixels = image.load()
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # XOR again with the same key to retrieve original values
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    
    image.save(output_path)
    print("Decryption complete.")

# Example usage:
key = 123
encrypt_image_xor("certs.jpg", "encrypted.jpg", key)
decrypt_image_xor("encrypted.jpg", "decrypted.jpg", key)
