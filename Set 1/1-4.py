import base64
import operator

with open('4.txt') as file:
    strings = file.readlines()


def fixedxor(hex1, char):
    b1 = bytes.fromhex(hex1)
    result = bytes(map(lambda x: x ^ char, b1))
    return result.decode(encoding="ascii", errors='ignore')


if __name__ == "__main__":
    lookup = {fixedxor(s, i): s for i in range(256) for s in strings}
    candidates = list(lookup.keys())
    candidates.sort(key=lambda x: -
                    len([1 for c in x if c.isalnum() or c == ' ']))
    for string in candidates[:5]:
        print(string, lookup[string])
