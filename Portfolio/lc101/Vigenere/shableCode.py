upperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerCase = ["a", "b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# which receives a letter (that is, a string with only one alphabetic character)
#  and returns the 0-based numerical position of that letter within the alphabet.

def alphabet_position(letter):
    # letter = letter.upper()
    if letter in upperCase:
        return(upperCase.index(letter))
    if letter in lowerCase:
        return(lowerCase.index(letter))

# write another helper function rotate_character(char, rot) which receives a character
# char (that is, a string of length 1), and an integer rot. Your function should return 
# a new string of length 1, the result of rotating char by rot number of places to the right.

def rotate_character(char, rot):
  if char in upperCase:
    ind = alphabet_position(char)
    return(upperCase[(ind + rot) % 26])

  if char in lowerCase:
    ind = alphabet_position(char)
    return(lowerCase[(ind + rot) % 26])
  else:
    return char

# print(rotate_character("c", 27))

# print(alphabet_position("z"))

# encrypt(text, rot), 
# which receives as input a string and an integer. 
# This is just like the rot13, instead of hardcoding the number 13, your function should receive a second argument, rot which specifies the rotation amount. 
# Your function should return the result of rotating each letter in the text by rot places to the right.
def encrypt(text, rot):
  newText = ""
  for letter in text:
    changedText = rotate_character(letter, rot)
    #" ".join(changedText)
    newText += "".join(changedText) 
  return("".join(newText))
  
print(encrypt("Hello World!", 5))