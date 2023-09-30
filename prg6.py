import sys

n = 5

key = [[11, 24, 31, 23, 21],
       [25, 14, 13, 18, 28],
       [15, 12, 16, 17, 19],
       [22, 26, 27, 29, 30],
       [32, 33, 34, 35, 36]]
msg = [[0] for _ in range(n)]
cipher = [[0] for _ in range(n)]

char_dict = {
    'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16,
    'g': 17, 'h': 18, 'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23,
    'n': 24, 'o': 25, 'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30,
    'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36
}

def generate_key_matrix(key_str):
    k = 0
    for i in range(n):
        for j in range(n):
            if key_str[k].isalpha():
                key[i][j] = char_dict[key_str[k]]
            elif key_str[k] == ' ':
                key[i][j] = 10
            elif key_str[k].isnumeric():
                key[i][j] = int(key_str[k])
            k += 1

def encrypt(msg_vector):
    for i in range(n):
        for j in range(1):
            cipher[i][j] = 0
            for x in range(n):
                cipher[i][j] += (key[i][x] * msg_vector[x][j])
            cipher[i][j] = cipher[i][j] % 37

def hill_cipher(ptext):
    k = 0
    for i in range(n):
        if ptext[i].isalpha():
            msg[i][0] = char_dict[ptext[i]]
        elif ptext[i] == ' ':
            msg[i][0] = 10
        elif ptext[i].isnumeric():
            msg[i][0] = int(ptext[i])
        k += 1
            
    encrypt(msg)

    CipherText = ''
    for i in range(n):
        if cipher[i][0] <= 9:
            CipherText += str(cipher[i][0])
        elif cipher[i][0] == 10:
            CipherText += ' '
        else:
            temp = [key for key, value in char_dict.items() if value == cipher[i][0]][0]
            CipherText += temp.upper()
   
    return CipherText

if len(sys.argv) < 2:
        print("Usage: python p6.py <plain_text>")
    
else:
        ptext = sys.argv[1]
        etext = ""
        k_word = "anumkodchrebfgilpqstvwxyz"

        while len(ptext) % 5 != 0:
            ptext += 'z'

        for i in range(0, len(ptext), 5):
            chunk = ptext[i:i+5]
            etext += hill_cipher(chunk)

        print("Plain text :", ptext)
        print("Encrypted text :", etext)
