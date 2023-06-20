from Crypto.Cipher import AES
import base64
import itertools

with open('8.txt') as file:
    strings = [bytes.fromhex(s) for s in file.readlines()]

def Hamming(s1, s2):
    return sum(map(lambda x, y: (x ^ y).bit_count(), s1, s2))

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def score(string):
    c = chunks(string, 16)
    combinations = list(itertools.combinations(c, 2))
    return sum(1 for b1, b2 in combinations if b1 == b2)
    
    
for string in sorted(strings, key=score):
    print(score(string), string.hex())
    