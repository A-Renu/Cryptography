import sys

def affine_cipher(ptext, a, b):
    etext = ""
    char_dict = {
        'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16,
        'g': 17, 'h': 18, 'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23,
        'n': 24, 'o': 25, 'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30,
        'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36
    }

    for char in ptext:
        if char.isalpha():
            char_value = char_dict[char]
            evalue = ((a * char_value) + b) % 37
        elif char == ' ':
            evalue = ((a * 10) + b) % 37
        else:
            char_value = ord(char) - ord('0')
            evalue = ((a * char_value) + b) % 37

        if evalue <= 9:
            etext += str(evalue)
        elif evalue == 10:
            etext += ' '
        else:
            echar = next((key for key, value in char_dict.items() if value == evalue), None)
            if echar is not None:
                etext += echar.upper()

    return etext

if len(sys.argv) < 2:
        print("Usage: python p2.py <plain_text>")
    
else:
        ptext = sys.argv[1]
        a = 3
        b = 1

        etext = affine_cipher(ptext, a, b)

        print("Plain text:", ptext)
        print("Encrypted text:", etext)
