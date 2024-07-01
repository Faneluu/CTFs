from DeHash import custom_hash_decrypt
import requests


input = ""  # Replace cu hex string-ul returnat de
byte_input = bytes.fromhex(input)
password = custom_hash_decrypt(byte_input)
print(custom_hash_decrypt(byte_input))


url = 'http://url:port/'
payload = {'password': password.decode('utf-8')}
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Cererea a fost efectuată cu succes!")
    print("Răspunsul serverului:", response.text)
else:
    print("Cererea a eșuat. Cod de stare:", response.status_code)

