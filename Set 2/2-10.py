from lib import *
import base64

plaintext = "CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks. "

encrypted = aescbcencrypt(plaintext.encode(encoding='ascii'), "YELLOW SUBMARINE".encode(encoding='ascii'))
decrypted = aescbcdecrypt(encrypted, "YELLOW SUBMARINE".encode(encoding='ascii'))

print(encrypted)
print(decrypted.decode(encoding='ascii'))

with open('10.txt') as file:
    plain = base64.b64decode(''.join(file.readlines()).replace('\n', ''))
decrypted = aescbcdecrypt(plain, "YELLOW SUBMARINE".encode(encoding='ascii'))

print(decrypted.decode(encoding='ascii'))