import random

print("welcome to game", end = " ")
print('''  
_ _                                         
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

#step1: creating a list of words
random_paragraph = "elephant dinosaur oxygen chocolate adventure galaxy kangaroo algorithm basketball butterfly library mountain whisper rainbow volcano rhythm symphony avalanche ecosystem architecture phoenix crocodile quarantine hurricane laboratory sapphire cryptography expedition renaissance tournament kaleidoscope"
word_list = random_paragraph.split()

alphabets = "abcdefghikjlmnopqrstuvwxyz"

#step2: obtaining a random word from our list
random_word = random.choice(word_list)
random_word = random_word.lower()

print()
print()
print()

print("you have to guess the random word before the man dies!")
print()


#step3: creating a char array with blank line(_)
length_of_word = len(random_word)
char_array = ""
for i in range(length_of_word):
    char_array += "_ "

print(char_array)
print()
print("this size of word is mentioned above with blanks")
print()

#step4: loop until man dies or word found

hangman_logo = [r"""
   +--+
   |  |
      |
      |
      |
      |
  =====""",
r"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
      |
  ====="""]

print("initial_condition : ")
print(hangman_logo[0])
print()

guessed_char = ""

for length in range(length_of_word):
  guessed_char += ' '

logo_state=1

def string_appending(guessed_char, value, index) :
    new_list = list(guessed_char)
    new_list[index] = value
    new_str = ""
    for values in new_list:
        new_str += values
    return new_str

entered_chars = ""

stored_word = random_word
while guessed_char != stored_word and logo_state < len(hangman_logo):
  guessed_letter = input("guess a letter in the word : ")
  if guessed_letter not in alphabets :
      print("abey bosedk , amma behen pe avunga!, sahi karo!")
  elif guessed_letter in entered_chars:
      print("you have already entered character")
  elif guessed_letter in random_word:
      while guessed_letter in random_word:
          index = random_word.find(guessed_letter)
          character = random_word[index]
          entered_chars += character
          random_word = string_appending(random_word, "_", index)
          guessed_char = string_appending(guessed_char, character, index)
          char_array = string_appending(char_array, character, index*2)
      print(char_array)
  else:
      entered_chars += guessed_letter
      print("you lost one life")
      print(hangman_logo[logo_state])
      logo_state += 1

#step5: final output
print("the word is", stored_word)
if guessed_char == stored_word:
    print("you won the game")
else:
    print("you lost the game")
print("have a nice day!")
input()