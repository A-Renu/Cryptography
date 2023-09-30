import sys

def convert_to_upper(text):
    return text.upper()

def remove_spaces(text):
    ntext = "".join(char for char in text if char != " ")
    return ntext

def vigenere_cipher(text, key):
    etext = [(chr((ord(text[i]) + ord(key[i])) % 26 + ord('A'))) for i in range(len(text))]
    return "".join(etext)

def generate_key(text, key):
    key_length = len(key)
    return key * (len(text) // key_length) + key[:len(text) % key_length]

if len(sys.argv) < 2:
        print("Usage: python p5.py <plain_text>")
    
else:
        ptext = remove_spaces(convert_to_upper(sys.argv[1]))
        k_word = "ANUMKODCHREBFGILPQSTVWXYZ"

        key = generate_key(ptext, k_word)
        etext = vigenere_cipher(ptext, key)

        print("Plain text :", ptext)
        print("Encrypted text :", etext)
