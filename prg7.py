import sys

char_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, ' ': 10, 'a': 11, 'b': 12, 'c': 13, 'd': 14,
    'e': 15, 'f': 16, 'g': 17, 'h': 18, 'i': 19, 'j': 20, 'k': 21,
    'l': 22, 'm': 23, 'n': 24, 'o': 25, 'p': 26, 'q': 27, 'r': 28,
    's': 29, 't': 30, 'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36
}

initial_mapping = [11, 23, 29, 20, 17, 20, 8, 6, 10, 19, 5, 1, 4, 4, 5, 7, 10, 10, 11, 11, 12, 12, 12, 12, 12, 33, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

def rotor_cipher(plaintext):
    ciphertext = ""

    for char in plaintext:
        e_val = (initial_mapping[char_dict[char]] + char_dict[char]) % 37
        echar = next((key for key, value in char_dict.items() if value == e_val), None)
        if echar is not None:
            ciphertext += echar.upper()
        Rotate(initial_mapping)
    return ciphertext

def Rotate(arr):
    p = 1
    while (p <= 1):
        last = arr[0]
        for i in range(36 - 1):
            arr[i] = arr[i + 1]
        arr[36 - 1] = last
        p = p + 1

if len(sys.argv) < 2:
    print("Usage: python p7.py <plain_text>")
else:
    ptext = sys.argv[1]
    etext = rotor_cipher(ptext)

    print("Plain text:", ptext)
    print("Encrypted text:", etext)
