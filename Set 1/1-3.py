import base64
import operator
import string


def fixedxor(hex1, char):
    b1 = bytes.fromhex(hex1)
    result = bytes(map(lambda x: x ^ char, b1))
    return result.decode(encoding="ascii", errors='ignore')


if __name__ == "__main__":
    strings = [fixedxor(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", i) for i in range(256)]
    strings.sort(key=lambda x: -
                 len([1 for c in x if c.isalnum() or c == ' ']))
    for string in strings[:5]:
        print(string)
