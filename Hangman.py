
import List as list
import random


word = random.choice(list.fruits or list.numbers)
user_guess = ""
length_of_word = len(word)
dashes_for_word = ""
word_complete = False



print(word)
print(length_of_word)


while word_complete == False:
    for n in range(length_of_word):
        dashes_for_word += "_"


    print(dashes_for_word)

    user_guess = str(input("Guess?"))

    word_complete = True








