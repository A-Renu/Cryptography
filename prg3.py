import sys

def autokey_cipher(ptext, a_key):
    etext = ""
    char_dict = {
        ' ': 10, 'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16,
        'g': 17, 'h': 18, 'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23,
        'n': 24, 'o': 25, 'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30,
        'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36
    }

    key = str(a_key)
    key += ptext
    key = key[:-1]

    for char1, char2 in zip(ptext, key):
        if char1.isalpha():
            evalue1 = char_dict[char1]
        elif char1 == ' ':
            evalue1 = 10
        else:
            evalue1 = int(char1)

        if char2.isalpha():
            evalue2 = char_dict[char2]
        elif char2 == ' ':
            evalue2 = 10
        else:
            evalue2 = int(char2)

        evalue = (evalue2 + evalue1) % 37

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
        print("Usage: python p3.py <plain_text>")
    
else:
        ptext = sys.argv[1]
        a_key = 3

        etext = autokey_cipher(ptext, a_key)

        print("Plain text:", ptext)
        print("Encrypted text:", etext)
