from Crypto.Cipher import AES
import base64

key = b'YELLOW SUBMARINE'

with open('7.txt') as file:
    string = base64.b64decode(''.join(file.readlines()).replace('\n', ''))

cipher = AES.new(key, AES.MODE_ECB)

print(cipher.decrypt(string).decode(encoding='ascii'))