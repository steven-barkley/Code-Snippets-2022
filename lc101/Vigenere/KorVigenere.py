def alphabet_position(letter):

    alphabet = list ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_2 = list('abcdefghijklmnopqrstuvwxyz')
    if letter in alphabet:
      return alphabet.index(letter)
    if letter in alphabet_2:
      return alphabet_2.index(letter)
    return letter

def rotate_character(char, rot):
  try:
    letter_index = alphabet_position(char) + rot
    letter_index = letter_index % 26
  except TypeError:
    return char
   
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  for i in range(0,len(alphabet)):
    if i == letter_index:
      if char in alphabet:
        return alphabet[i]

      if char in alphabet_2:
        return alphabet_2[i]

def encrypt(text,key):
  alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

  encrypted = []    
  starting_index = 0
  
  for letter in text:
        
        rotation = alphabet_position(key[starting_index])
        
        if not letter in alphabet:
            encrypted.append(letter)
            
        elif letter.isalpha()   :            
            encrypted.append(rotate_character(letter, rotation))

        if starting_index == (len(key) - 1): 
            starting_index = 0
        else: 
            starting_index +=1

        

  return "".join(encrypted)

    


print(encrypt("The crow flies at midnight!","boom"))    