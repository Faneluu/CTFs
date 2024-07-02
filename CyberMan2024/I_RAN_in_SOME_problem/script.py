from Crypto.Cipher import AES
import os

def decrypt_file(file_path, key, iv, output_path):

    # Read the encrypted data from the file
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    # Create the AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove padding (PKCS7 padding)
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    # Write the decrypted data to the output file
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"File decrypted and saved to {output_path}")

# Example usage
# Define the file paths and the key/iv
file_path = 'flag.enc'
output_path = 'decrypted_file.bin'
key = bytes.fromhex("7375703334733363723374703473737730726468316464336e66723330434243")  # Replace with your hexadecimal key
iv = bytes.fromhex('6976666f7270617373776f7264435446')

# Call the decrypt_file function
decrypt_file(file_path, key, iv, output_path)
