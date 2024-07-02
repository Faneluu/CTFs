import requests
from Crypto.Cipher import AES

def remove_padding(input_string, padding_char='\x00'):
    return input_string.rstrip(padding_char.encode("utf-8"))


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text


def hash_decrypt(hashed_value):
    chunk1 = hashed_value[:16]
    chunk2 = hashed_value[16:]
    key = b'KGS!@#$%KGS!@#$%'
    dchunk1 = decrypt(chunk1, key)
    dchunk2 = decrypt(chunk2, key)
    padded_string = dchunk1 + dchunk2
    input_string = remove_padding(padded_string)
    return input_string

input = "ff03876031b2c4aaca9634ddac5ebc0242631272eeaffc42fbdfd097607fc3a2"
byte_input = bytes.fromhex(input)
password = hash_decrypt(byte_input)
print(password)


url = 'http://10.2.0.26:48670/'
payload = {'password': password.decode('utf-8')}
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Cererea a fost efectuată cu succes!")
    print("Răspunsul serverului:", response.text)
else:
    print("Cererea a eșuat. Cod de stare:", response.status_code)

