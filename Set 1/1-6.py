import base64
import operator
import statistics
from collections import defaultdict

letterFrequency = defaultdict(lambda : - 10.0)
letterFrequency.update({
' ' : 20,
'e' : 12.0,
't' : 9.10,
'a' : 8.12,
'o' : 7.68,
'i' : 7.31,
'n' : 6.95,
's' : 6.28,
'r' : 6.02,
'h' : 5.92,
'd' : 4.32,
'l' : 3.98,
'u' : 2.88,
'c' : 2.71,
'm' : 2.61,
'f' : 2.30,
'y' : 2.11,
'w' : 2.09,
'g' : 2.03,
'p' : 1.82,
'b' : 1.49,
'v' : 1.11,
'k' : 0.69,
'x' : 0.17,
'q' : 0.11,
'j' : 0.10,
'z' : 0.07 })


def fixedxor(hex1, char):
    result = bytes(map(lambda x: x ^ char, hex1))
    return result.decode(encoding="ascii", errors='replace')

def getkey(b1, s2):
    b2 = s2.encode(encoding='ascii')
    result = bytes(map(operator.xor, b1, b2))
    return result.decode(encoding='ascii')

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with open('6.txt') as file:
        string = base64.b64decode(''.join(file.readlines()).replace('\n', ''))

def transpose(s, KEYSIZE):
    return [s[i::KEYSIZE] for i in range(KEYSIZE)]

rankings = dict()

def Hamming(s1, s2):
    return sum(map(lambda x, y: (x ^ y).bit_count(), s1, s2))


if __name__ == "__main__":
    for KEYSIZE in range(4, 41):
        hchunks = [string[i*KEYSIZE:(i+1)*KEYSIZE] for i in range(4)]
        hammings = [Hamming(s1, s2) for (s1, s2) in zip(hchunks, hchunks[1:])]
        rankings[statistics.mean(hammings)/KEYSIZE] = KEYSIZE

    for rank in list(sorted(rankings.keys())):
        print(rank, '-', rankings[rank])
        KEYSIZE = rankings[rank]
        chunks = transpose(string, KEYSIZE)
        bests = list()
        for chunk in chunks:
            candidates = [fixedxor(chunk, i) for i in range(0,256)]
            candidates.sort(key=lambda x: 
                            -sum([letterFrequency[c] for c in x.lower()]))
            bests.append(candidates[0])
        solution = ''.join(''.join(c) for c in zip(*bests))
        print(solution)
        print(getkey(string, solution))
            
        None
