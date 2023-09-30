import sys

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def key_table(key, char_list):
    kchar = []
    for char in key:
        if char not in kchar:
            kchar.append(char)

    temp = []
    for char in kchar:
        if char not in temp:
            temp.append(char)
    for char in char_list:
        if char not in temp:
            temp.append(char)

    matrix = [temp[i:i+5] for i in range(0, len(temp), 5)]
    return matrix

def find(matrix, x):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == x:
                return i, j

def row(matrix, row1, col1, row2, col2):
    char1 = matrix[row1][(col1 + 1) % 5]
    char2 = matrix[row2][(col2 + 1) % 5]
    return char1, char2

def column(matrix, row1, col1, row2, col2):
    char1 = matrix[(row1 + 1) % 5][col1]
    char2 = matrix[(row2 + 1) % 5][col2]
    return char1, char2

def rectangle(matrix, row1, col1, row2, col2):
    char1 = matrix[row1][col2]
    char2 = matrix[row2][col1]
    return char1, char2

def playfair_cipher(matrix, diagraph_list):
    extext = []
    for diagraph in diagraph_list:
        char1 = 0
        char2 = 0
        row1, col1 = find(matrix, diagraph[0])
        row2, col2 = find(matrix, diagraph[1])

        if row1 == row2:
            char1, char2 = row(matrix, row1, col1, row2, col2)
        elif col1 == col2:
            char1, char2 = column(matrix, row1, col1, row2, col2)
        else:
            char1, char2 = rectangle(matrix, row1, col1, row2, col2)

        epair = char1 + char2
        extext.append(epair)
    return extext

def convert_to_lower(text):
    return text.lower()

def remove_spaces(text):
    ntext = "".join(char for char in text if char != " ")
    return ntext

def pair(text):
    diagraphs = []
    group = 0
    for i in range(2, len(text), 2):
        diagraphs.append(text[group:i])
        group = i
    diagraphs.append(text[group:])
    return diagraphs

def fill(text):
    k = len(text)
    for i in range(0, k-1, 2):
        if text[i] == text[i+1]:
            ntext = text[0:i+1] + 'x' + text[i+1:]
            ntext = fill(ntext)
            break
        else:
            ntext = text
    return ntext

if len(sys.argv) < 2:
        print("Usage: python p4.py <plain_text>")
    
else:
        ptext = sys.argv[1]

        char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        ptext = fill(remove_spaces(convert_to_lower(ptext)))

        if len(ptext) % 2 != 0:
            ptext += 'z'

        key = "anumkodchrebfgilpqstvwxyz"

        key_square = [
                        ['a', 'n', 'u', 'm', 'k'],
                        ['o', 'd', 'c', 'h', 'r'],
                        ['e', 'b', 'f', 'g', 'i'],
                        ['l', 'p', 'q', 's', 't'],
                        ['u', 'w', 'x', 'y', 'z']
        ]

        diagraph_list = pair(ptext)
        output_list = playfair_cipher(key_square, diagraph_list)

        etext = "".join(output_list).upper()

        print("Plain Text:", ptext)
        print("Cipher Text:", etext)
