import lib
import random


with open("lyrics.txt", "rb") as file:
    plaintext = file.read()

def random_key():
    return random.randbytes(16)

def randomizer(b):
    cipher = random.choice([lib.ecbencrypt, lib.cbcencrypt])
    key = random_key()
    padded = lib.align(random.randbytes(random.randrange(5, 11)) + b + random.randbytes(random.randrange(5, 11)))
    print(cipher)
    return cipher(padded, key)

for i in range(10):
    print(lib.oracle(randomizer(plaintext)))