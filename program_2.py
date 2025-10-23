##
# Code by: Parker Jolly
# On: 10/23/2025
# Program name: Word Seperator
##

def word_separator(sentence):

    new_sentence = ""

    for i in range(len(sentence)):
        # Add letters to new_sentence
        if i == 0:
            # Capitalize first letter
            new_sentence += sentence[i].upper()
        elif sentence[i].isupper():
            # Add spaces when we find a capital letter, and then make it lowercase
            new_sentence += " " + sentence[i].lower()
        else:
            # Add letter to new_sentence
            new_sentence += sentence[i]

    # Remove whitespaces and add period
    new_sentence = new_sentence.strip() + "."

    return new_sentence

# Run code

sentence = input("Enter a sentence with no spaces or punctuation and the first letter of every word capitalized: ")

new_sentence = word_separator(sentence)

print(new_sentence)