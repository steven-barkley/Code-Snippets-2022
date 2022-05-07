lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet_position(letter):
    if letter in lowercase_alphabet:
        lower = lowercase_alphabet.index(letter)
        return lower

    if letter in uppercase_alphabet:
        upper = uppercase_alphabet.index(letter)    
        return upper

def rotate_character(char, rot):
    if char.isalpha() == False:
       return char   
    num_of_rot = alphabet_position(char) + rot
    #print(num_of_rot)
    crypto = ""
    if char in lowercase_alphabet:
        if num_of_rot < 26:
            crypto = crypto + lowercase_alphabet[num_of_rot]
        else:
            crypto = lowercase_alphabet[num_of_rot % 26]
        return crypto
     
    #for i in uppercase_alphabet:
    if char in uppercase_alphabet:
        if num_of_rot < 26:
            crypto += uppercase_alphabet[num_of_rot]
        else:
            crypto += uppercase_alphabet[num_of_rot % 26]
        return crypto  

def encrypt(text, encryption_key):

    secret_mess = ''
    for x in text:
        for i in encryption_key:
            b = alphabet_position(i)
            print(b)
            a = rotate_character(x, alphabet_position(i))
            print(a)
            secret_mess += a
        return secret_mess 