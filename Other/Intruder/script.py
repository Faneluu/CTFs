from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import itertools

# Your ciphertext goes here
ciphertext = bytes.fromhex("bd85fd185676dd40d84e3572d6d3c6670b39f44a58c6e4d12be59db274956cb8c74a10a44ca7af0244e5b3e2ee84994449ca3dadf58d11c9a32f142dca2182b3aa9dc571d23399380d1b94ed448bc332")  # Replace with your actual ciphertext in hex format

# Prepare the buffer_256
buffer_256 = bytearray(range(256))

# IV is 0
iv = bytes([0] * 16)

# Brute-force the key
for random_byte in range(256):
    key = buffer_256[random_byte:random_byte+16]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        if decrypted.startswith(b"CTF{"):
            print(f"Key found: {key.hex()}")
            print(f"Decrypted text: {decrypted.decode()}")
            break
    except (ValueError, KeyError):
        # Handle padding errors and incorrect keys
        continue
