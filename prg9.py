import sys

def keyless_tranposition_cipher(ptext, width):
    ptext = ptext.replace(" ", "").upper()
    num_rows = (len(ptext) + width - 1) // width

    matrix = [[' ' for _ in range(width)] for _ in range(num_rows)]

    index = 0
    for row in range(num_rows):
        for col in range(width):
            if index < len(ptext):
                matrix[row][col] = ptext[index]
                index += 1

    etext = ''
    for col in range(width):
        for row in range(num_rows):
            etext += matrix[row][col]

    return etext

if len(sys.argv) < 2:
    print("Usage: python p9.py <plain_text>")
    
else:
    ptext = sys.argv[1]
    width = 3

    etext = keyless_tranposition_cipher(ptext, width)
    
    print("Plain text:", ptext)
    print("Encrypted text:", etext)
