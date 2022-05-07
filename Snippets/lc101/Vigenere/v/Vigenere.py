def alphabet_position(letter):    
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cap_alpha = alpha.upper()

    if letter.isupper(): 
        return cap_alpha.index(letter)
    else:
        return alpha.index(letter)    

#print(alphabet_position("r"))

def rotate_character(char, rot):

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cap_alpha = alpha.upper()
    
    if char.isalpha():
        rotated_index = alphabet_position(char) + rot
        if char.isupper():
            if rotated_index < 26:
                return cap_alpha[rotated_index]
            else:
                return cap_alpha[rotated_index % 26]
        else:
            if rotated_index < 26:
                return alpha[rotated_index]
            else:
                return alpha[rotated_index % 26]
    else:
        return char

#print(rotate_character(",", 29))

def encrypt(text, key):

    encrypted = ''
    index = 0
    for char in text:
        if char.isalpha():
            for letter in key:#(len(key)-1):
                rot = alphabet_position(letter)
                if key[index] < (len(key)-1):
                    index += 1
                else:
                    index = 0
        encrypted += rotate_character(char, rot)
    return encrypted

print(encrypt("The crow flies at midnight!", "boom"))