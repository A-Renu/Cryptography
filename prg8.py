import sys

def rail_fence_cipher(ptext, key):
    fence = [[''] * (len(ptext) * 2) for _ in range(key)]
    rail = 0
    direction = 1
    index = 0

    for char in ptext:
        fence[rail][index] = char
        index += 1
        rail += direction

        if rail == key - 1 or rail == 0:
            direction = -direction

    cipher_text = ''.join([''.join(row) for row in fence])
    return cipher_text

if len(sys.argv) < 2:
    print("Usage: python p8.py <plain_text>")
else:
    ptext = sys.argv[1]
    key = 3

    etext = rail_fence_cipher(ptext, key)

    print("Plain text :", ptext)
    print("Encrypted text :", etext.upper())
