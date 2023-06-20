from Crypto.Cipher import AES
from random import randbytes
import itertools


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def oracle(b):
    c = chunks(b, 16)
    combinations = list(itertools.combinations(c, 2))
    return sum(1 for b1, b2 in combinations if b1 == b2) == 0

def bxor(b1, b2): # use xor for bytes
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return result

def pad(b, size=16, char=b'\x04'):
    return b.ljust(size, char)

def align(b):
    if len(b) % 16:
        return pad(b, 16*(1+len(b)//16))
    return b

def ecbencrypt(b, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(b)

def cbcencrypt(b, key):
    cipher = AES.new(key, AES.MODE_CBC, randbytes(16))
    return cipher.encrypt(b)

def aescbcencrypt(b, key, iv=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
    cipher = AES.new(key, AES.MODE_ECB)
    prev = iv
    result = list()
    for index in range(0, len(b), 16):
        chunk = pad(b[index:min(index+16, len(b))], 16)
        chunk = bxor(chunk, prev)
        encrypted = cipher.encrypt(chunk)
        prev = encrypted
        result.append(encrypted)
    return b''.join(result)

def aescbcdecrypt(b, key, iv=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
    cipher = AES.new(key, AES.MODE_ECB)
    prev = iv
    result = list()
    for index in range(0, len(b), 16):
        chunk = pad(b[index:min(index+16, len(b))], 16)
        decrypted = cipher.decrypt(chunk)
        result.append(bxor(decrypted, prev))
        prev = chunk
    return b''.join(result)

