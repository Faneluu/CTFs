from Crypto.Cipher import AES


key = b'KGS!@#$%KGS!@#$%'


def split_string(s):
    return [s[:16], s[16:]]


def add_padding(input_string, length, padding_char='\x00'):
    if len(input_string) >= length:
        return input_string
    else:
        return input_string + padding_char * (length - len(input_string))


def custom_hash(input_string):
    input_string_uppercase = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            input_string_uppercase += chr(ord(char) - 32)
        else:
            input_string_uppercase += char

    padded_string = add_padding(input_string_uppercase, 32)

    chunk1, chunk2 = split_string(padded_string)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_chunk1 = cipher.encrypt(chunk1.encode())
    encrypted_chunk2 = cipher.encrypt(chunk2.encode())
    return encrypted_chunk1 + encrypted_chunk2
