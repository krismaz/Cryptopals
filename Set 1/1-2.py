import base64
import operator


def fixedxor(hex1, hex2):
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
    result = bytes(map(operator.xor, b1, b2))
    return result.hex()


if __name__ == "__main__":
    print(fixedxor("1c0111001f010100061a024b53535009181c",
          "686974207468652062756c6c277320657965"))
