import sys

def caeser_cipher(ptext, shift):
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
            evalue = (char_value + shift) % 37
        elif char == ' ':
            evalue = (10 + shift) % 37
        else:
            char_value = ord(char) - ord('0')
            evalue = (char_value + shift) % 37

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
        print("Usage: python p1.py <plain_text>")
    
else:
        ptext = sys.argv[1]
        shift = 3

        etext = caeser_cipher(ptext, shift)

        print("Plain text:", ptext)
        print("Encrypted text:", etext)
