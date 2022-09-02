import base64
import operator


def fixedxor(s1, s2):
    s2 = (s2*(len(s1)//len(s2) + 1))[:len(s1)]
    b1 = s1.encode(encoding="ascii")
    b2 = s2.encode(encoding="ascii")
    result = bytes(map(operator.xor, b1, b2))
    return result.hex()


if __name__ == "__main__":
    print(fixedxor("""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""",
          "ICE"))
