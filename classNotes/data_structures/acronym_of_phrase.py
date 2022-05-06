'''         Find acronym of a phrase
Take a phrase from user and convert that phrase to the acronym.
Example: if user enters "national university of science and technoology"
It should be converted to NUOSAT





'''
phrase = input("Enter a phrase: ")

phrase = phrase.strip()

phrase = phrase.upper()

words = phrase.split(" ")

letters = []
for word in words:
    letters.append(word[0])

acronym = ''.join(letters)

print(acronym)  # NUOSAT
