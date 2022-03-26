def translate(text):
# your code here!
   english_2_pirate = {'sir': 'matey','hotel':'fleabag inn', 'student':'swabbie','boy':'matey','madam':'proud beauty','professor':'foul blaggart','restaurant':'galley','your':'yer','excuse':'arr','students':'swabbies','are':'be','lawyer':'foul blaggart','the':'th','restroom':'head','my':'me','hello':'avast','is':'be','man':'matey'}
   new_word = ''
   sentence = (text.split())
   sentence_no_char = []
   sentence_pirate = []
   for i in sentence:
       if i.isalpha():
           sentence_no_char.append(i)
       else:
           sentence_no_char.append(i.split(",")[0])

   for j in sentence_no_char:
       if j in english_2_pirate:
           new_word = english_2_pirate[j]
       else:
           new_word = j
       sentence_pirate.append(new_word)

   glue = " "
   string = glue.join(sentence_pirate)
   print (string)
text = "hello my man, please excuse your professor to the restroom!"
#testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")
translate(text)