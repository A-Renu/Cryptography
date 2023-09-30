import sys

key_permute = [11, 24, 31, 23, 21, 25, 14, 13, 18, 28, 15, 12, 16, 17, 19, 20, 22, 26, 27, 29, 30, 32, 33, 34, 35, 36, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def keyed_transposition_cipher(ptext):
    length = len(ptext)
    etext = [''] * length
    for i in range(length):
        etext[i] = ptext[key_permute[i]]

    return ''.join(etext)

if len(sys.argv) < 2:
    print("Usage: python p10.py <plain_text>")
    
else:
    ptext = sys.argv[1]
    n = len(ptext)
    if n < 37:
        ptext += 'z' * (37 - n)
        
    etext = keyed_transposition_cipher(ptext)
    
    print("Plain text:", ptext)
    print("Encrypted text:", etext)
